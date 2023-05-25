import re
import xml.etree.ElementTree as ET
import csv

# Parse the XML file
tree = ET.parse('depth02_template_b_1.feb')
root = tree.getroot()

# Find all SolidDomain elements
solid_domains = root.findall('.//MeshDomains/SolidDomain')

# Open the CSV file
with open('sample_short.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row

    for j, row in enumerate(reader):
        for i, domain in enumerate(solid_domains[1:]):
            if i >= 49:
                continue
            domain.set('mat', str(row[i]))

        # Save modified XML to a new file
        new_file_name = f"depth02_template_b_{j*10}.feb"

        # Write modified XML to file
        with open(new_file_name, 'w', encoding='ISO-8859-1') as output_file:
            tree.write(output_file, encoding='ISO-8859-1', xml_declaration=True)
