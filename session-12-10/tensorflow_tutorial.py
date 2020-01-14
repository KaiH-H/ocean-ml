from __future__ import absolute_import, division, print_function, unicode_literals 
import warnings
with warnings.catch_warnings():
		warnings.filterwarnings("ignore",category=FutureWarning)
		import tensorflow as tf
		from tensorflow.keras import datasets, layers, models
		import matplotlib.pyplot as plt

# rest of code from tutorial 

# Loading the data from the CIFAR10 dataset
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# Normalize pixel values to be between 0 and 1
# Pixel values are typically between 0 and 255 (0 = black, 255 = white)
train_images, test_images = train_images / 255.0, test_images / 255.0

# Adds labels to each class(image)
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

# Shows the images with their class names
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    # The CIFAR labels happen to be arrays, 
    # which is why you need the extra index
    plt.xlabel(class_names[train_labels[i][0]])
plt.show()

# Creates a model variable and adds layers of neurons to the network 
# ex. (32, 32, 3) refers to the RGB values
model = models.Sequential()

# Convolutional layers tell the algorithm which pixels are next to each other
# 32 filters with a filter of 3x3 (kernal = filter)
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))

# Max Pooling takes the maximum value in the grouping parameter you set and stores it
model.add(layers.MaxPooling2D((2, 2))) 
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

# Shows what the network looks like
model.summary()

# Flatten = Makes the 3D into 1D (it's like unrolling it) --> Puts in in a 'row'
# Dense = Makes everything in the 'row' into the neural network (performs the classification)
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax')) # 10 classifications

model.summary()

# Makes the model and trains it 
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(train_images, train_labels, epochs=10, 
                    validation_data=(test_images, test_labels))

# Graphs the accuracy of the model 
plt.plot(history.history["accuracy"], label='accuracy')
plt.plot(history.history["val_accuracy"], label = 'val_accuracy')
plt.xlabel('Epoch') # Epochs are basically batches of the training set --> Model cannot train everything at once
plt.ylabel('Accuracy') # Accuracy was how accurate the training was
plt.ylim([0.5, 1])
plt.legend(loc='lower right')

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

# Prints the accuracy of the network
print(test_acc)

