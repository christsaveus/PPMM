import re
import xml.etree.ElementTree as ET
import csv
# This code aims to get the index of SolidDomain and changed the attribute from the empty to the specific property.

tree = ET.parse('depth02_template_b_1.feb')
root = tree.getroot()

solid_domains = root.findall('.//MeshDomains/SolidDomain')

with open('sample_short.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for j, row in enumerate(reader):
        for i, domain in enumerate(solid_domains[1:]):
            if i >= 49:
                continue
            domain.set('mat', str(row[i]))
        
        # new_file_name = f"depth02_template_b_{j*10}.feb"
        new_file_name = f"depth02_template_b_dummy.feb"
        tree.write(new_file_name)