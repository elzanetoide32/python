import tensorflow as tf

constante=tf.constant([2.0,3,4],dtype=tf.float32, name='Constante1')

print(constante)


apartado=tf.placeholder(tf.float32, name='Apartado1')

print(apartado)
Tensor("Apartado1:0", dtype=float32)

variable=tf.Variable(3,dtype=tf.float32,name='variable1')

print(variable)


matriz=tf.zeros([3, 4], tf.int32, name='matriz')

print(matriz)
Tensor("matriz:0", shape=(3, 4), dtype=int32)
inicializar=tf.global_variables_initializer()

sess=tf.Session()

sess.run(inicializar)

print(sess.run(variable))


multiplicacion=apartado*constante

print(sess.run(multiplicacion,feed_dict={apartado:[[15,10,5]]}))


