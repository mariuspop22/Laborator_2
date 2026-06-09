import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train / 255.0
X_test = X_test / 255.0

print("Shape train:", X_train.shape)
print("Shape test:", X_test.shape)

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

history = model.fit(
    X_train, y_train,
    epochs=5,
    validation_data=(X_test, y_test)
)

test_loss, test_acc = model.evaluate(X_test, y_test)
print("\nTest accuracy:", test_acc)

index = 0

img = X_test[index]
label = y_test[index]

prediction = model.predict(img.reshape(1, 28, 28))
pred_class = np.argmax(prediction)

plt.imshow(img, cmap='gray')
plt.title(f"Real: {label} | Predictie: {pred_class}")
plt.show()


model2 = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model2.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model2.fit(X_train, y_train, epochs=5, verbose=0)

acc2 = model2.evaluate(X_test, y_test, verbose=0)[1]
print("\nAccuracy model cu 32 neuroni:", acc2)

model3 = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model3.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model3.fit(X_train, y_train, epochs=1, verbose=0)
acc3 = model3.evaluate(X_test, y_test, verbose=0)[1]
print("\nAccuracy cu 1 epoca:", acc3)


model4 = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='tanh'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model4.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model4.fit(X_train, y_train, epochs=5, verbose=0)

acc4 = model4.evaluate(X_test, y_test, verbose=0)[1]
print("\nAccuracy cu tanh:", acc4)
