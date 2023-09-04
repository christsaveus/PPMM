from abaqus import *
from abaqusConstants import *
from driverUtils import executeOnCaeStartup
import csv
import os
import shutil

# Get the current working directory
current_dir = os.getcwd()

executeOnCaeStartup()

session.viewports['Viewport: 1'].setValues(displayedObject=None)

with open('sample_7by7_100.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)
    data = list(reader)

# Prepare a list to store displacements
displacements = []
reaction_forces = []

for i in range(1,len(data)+1):
    odb_path = os.path.join(current_dir, 'template-{}.odb'.format(i))

    odb = session.openOdb(name=odb_path)

    session.viewports['Viewport: 1'].setValues(displayedObject=odb)

    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF, ))
    
    stepName = 'Step-1'

    step = odb.steps[stepName]

    frame = step.frames[-1]
    # lastFrame = odb.steps[stepName].frames[-1]
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=stepName, frame=-1)
    rp_node = odb.rootAssembly.nodeSets['RP_COUPLING']
    displacement_field = frame.fieldOutputs['U']
    displacement_at_rp = displacement_field.getSubset(region=rp_node).values[0]

    # u1, u2, u3 = displacement_at_rp.data

    u2 = displacement_at_rp.data[1]

    displacements.append(u2)
    reaction_force_field = frame.fieldOutputs['RF']
    reaction_force_at_rp = reaction_force_field.getSubset(region=rp_node).values[0]
    rf2 = reaction_force_at_rp.data[1]
    reaction_forces.append(rf2)



    # Set print options for saving the image
    # session.printOptions.setValues(reduceColors=False, vpBackground=False, displayColors=ON , vpScaled=True, vpBackgroundStyle=TRANSPARENT, saveTiled=False)

    output_filename= 'OutputImage_%s.png' % i
    # session.printToFile(fileName=output_filename, format=PNG, canvasObjects=(session.viewports['Viewport: 1'],))

    # odb.close()

    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(triad=OFF, legend=OFF, title=OFF, state=OFF, annotations=OFF, compass=OFF)

    session.printOptions.setValues(rendition=BLACK_AND_WHITE, vpDecorations=OFF)
    session.viewports['Viewport: 1'].odbDisplay.basicOptions.setValues(pointElements=OFF, referencePoints=OFF, pc3dElements=OFF, pd3dElements=OFF)

    # output_filename= 'OutputImage_%s.png' % i
    # session.printToFile(fileName=output_filename, format=PNG, canvasObjects=(session.viewports['Viewport: 1'],))
    session.pngOptions.setValues(imageSize=(1920, 1515))
    # session.printToFile(fileName='001', format=PNG, canvasObjects=(
    # session.viewports['Viewport: 1'], ))
    session.printToFile(fileName=output_filename, format=PNG, canvasObjects=(session.viewports['Viewport: 1'],))


    odb.close()

for i, row in enumerate(data):
    row.append(displacements[i])
    row.append(reaction_forces[i])

# Add the new header
headers.append('displacement')
headers.append('reaction_force')

# Move the image files to the "images" folder
def move_files(src_dir, dst_dir, file_extension):
    # check if the destination folder exists, if not create it
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    # get all fiels from teh source directory
    for file_name in os.listdir(src_dir):
        # construct full file path
        src = os.path.join(src_dir, file_name)
        dst = os.path.join(dst_dir, file_name)
        #move file to destination directory
        if os.path.isfile(src) and file_name.endswith(file_extension):
            shutil.move(src, dst)

# specify source and destination directories
dst_dir = "images"
file_extension = '.png'

# move the files using function
move_files(current_dir, dst_dir, file_extension)




os.mkdir(os.path.join(current_dir, "csv"))

with open(os.path.join(os.path.join(current_dir, "csv"), 'sample_ver_100_2.csv'), 'w') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data)