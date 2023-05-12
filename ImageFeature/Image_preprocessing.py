import tensorflow as tf
import tensorflow_addons as tfa
import matplotlib.pyplot as plt

# Load an image from file
img = tf.io.read_file('sample003.jpg')
img = tf.image.decode_jpeg(img, channels=3)

# Convert the image to grayscale
gray = tf.image.rgb_to_grayscale(img)

# Apply a binary threshold to the grayscale image
thresh = tf.where(gray < 100, 0, 255)

# Find connected components in the binary image
labels = tfa.image.connected_components(thresh)

# Extract the outermost contour of each connected component
contours = []
for i in tf.range(tf.reduce_max(labels)):
    component_mask = tf.where(labels == i + 1, 1, 0)
    contour = tf.image.find_contours(component_mask, 0.5)[0]
    contours.append(contour)

# Draw the outermost contour on the original image
plt.imshow(img.numpy())
plt.axis('off')
for contour in contours:
    plt.plot(contour[:, 1], contour[:, 0], 'g', linewidth=3)
plt.show()
