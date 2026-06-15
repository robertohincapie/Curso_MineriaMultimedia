# Unidad 1 — Fundamentos de Deep Learning para Datos No Estructurados

## Idea central
Comprender cómo entrenar modelos neuronales modernos para procesar datos no estructurados.

## Pregunta guía
¿Cómo aprenden las redes neuronales a partir de ejemplos?

## Objetivos
- Comprender la representación mediante tensores.
- Implementar modelos en PyTorch.
- Construir pipelines completos de entrenamiento.
- Diagnosticar problemas de generalización.

# Introducción a PyTorch, Tensores

## Introducción

Los tensores constituyen la estructura de datos fundamental de PyTorch y, en general, del Deep Learning moderno.

Desde un punto de vista computacional, un tensor puede entenderse como una generalización de los arreglos multidimensionales de NumPy hacia un entorno orientado al aprendizaje automático.

De hecho, PyTorch fue diseñado con una sintaxis muy similar a NumPy, por lo que la mayoría de las operaciones familiares para el estudiante continúan siendo válidas.

La principal diferencia es que los tensores incorporan capacidades adicionales que resultan esenciales para entrenar redes neuronales:

- almacenamiento en CPU o GPU,
- cálculo automático de gradientes,
- integración con el sistema de optimización.

---

## Dimensiones de un tensor

Los tensores pueden poseer cualquier número de dimensiones:

| Objeto | Dimensión |
|--------|------------|
| Escalar | 0D |
| Vector | 1D |
| Matriz | 2D |
| Tensor | nD |

En Deep Learning es común trabajar con tensores de tres, cuatro o incluso más dimensiones.

Por ejemplo:

- una imagen en escala de grises:

```text
(28, 28)
```

- una imagen RGB:

```text
(3, 224, 224)
```

- un lote de imágenes:

```text
(batch_size, 3, 224, 224)
```

---

## Forma (*shape*)

Todo tensor posee una forma o *shape*:

```python
X.shape
```

que puede producir:

```python
torch.Size([64, 3, 224, 224])
```

La forma determina:

- el número de observaciones,
- el tamaño de entrada del modelo,
- el consumo de memoria,
- la compatibilidad entre operaciones.

Comprender las dimensiones de los tensores es una de las habilidades más importantes al construir modelos de Deep Learning.

- REVISAR: - NUEVO: Shapes, Libro del manejo de los shapes de los tensores. view, reshape, unsqueeze, squeeze, etc. flatten. 

---

## Tensores y dispositivos

Una característica fundamental de PyTorch es que los tensores pueden almacenarse en diferentes dispositivos de cómputo.

Principalmente:

- memoria principal de la CPU,
- memoria de la GPU.

El usuario decide explícitamente dónde desea almacenar cada tensor.

Por ejemplo:

```python
device = torch.device(
    "cuda" if torch.cuda.is_available()
    else "cpu"
)

X = X.to(device)
```

Esta flexibilidad permite aprovechar la capacidad de procesamiento paralelo de las GPUs para acelerar el entrenamiento de modelos complejos.

Todos los tensores que participan en una misma operación deben encontrarse en el mismo dispositivo.

---

## Tensores y gradientes

Una de las características más importantes de los tensores en PyTorch es su capacidad para participar en el cálculo automático de derivadas.

Esto se controla mediante el parámetro:

```python
requires_grad=True
```

Por ejemplo:

```python
x = torch.tensor(
    [1.0, 2.0],
    requires_grad=True
)
```

Cuando un tensor tiene habilitado el cálculo de gradientes, PyTorch registra todas las operaciones realizadas sobre él y construye internamente un grafo computacional.

Posteriormente, durante el entrenamiento, estos gradientes son utilizados para actualizar los parámetros del modelo mediante algoritmos de optimización como descenso de gradiente.

En particular, los parámetros de las redes neuronales son tensores que almacenan:

- valores numéricos (pesos),
- gradientes asociados,
- información sobre el dispositivo donde residen.

Practiquemos un poco en el uso de tensores: 
- Miremos el uso básico de tensores de pytorch en el siguiente libro: [Libro 1.1 - Tensores 1](./libro11.ipynb)
- Otro libro para entender más en detalle el concepto de los tensores: [Libro 1.2 - Tensores 2](./libro12.ipynb)
- Un libro más avanzado de tensores: [Libro 1.3 - Tensores 3](./libro13.ipynb)
- Comprendamos con este libro el concepto del autograd: [Libro 1.4 - Autograd](./libro14.ipynb)

---

## Tensores como elemento unificador de PyTorch

En PyTorch prácticamente todo es un tensor:

- datos de entrada,
- imágenes,
- texto tokenizado,
- parámetros del modelo,
- gradientes,
- predicciones,
- funciones de pérdida.

Por ello, comprender la manipulación, dimensiones y almacenamiento de tensores constituye la base sobre la cual se construyen los sistemas modernos de aprendizaje profundo.

Cuando se construye una expresión, se construye un árbol computacional. Este puede verse en el libro [Libro 2: árboles computacionales](./libro2.ipynb)

Por ejemplo, podemos considerar los tensores para calcular el proceso de una regresión de manera numérica. Miremos este ejemplo en el siguiente libro: [Libro 3: regresión utilizando el gradiente en pytorch](./libro3.ipynb)

Miraremos conceptualmente un modelo de una red neuronal, que próximanente entenderemos más en detalle. La red neuronal (NN) se construye utilizando componentes, lineales de una red secuencial en este caso y funciones de activación. Alrededor de ella, necesitamos una función de error, unos parámetros del modelo. Un sistema de carga de los datos y un iterador que nos permita hacer el proceso del gradiente varias veces. Miremos la implementación en este libro: [Libro 4: red neuronal básica](./libro4.ipynb)

# Redes neuronales:  

Las redes neuronales son un modelo computacional inspirado en el funcionamiento del cerebro humano. Se utilizan en el campo de la inteligencia artificial para realizar tareas específicas, como reconocimiento de patrones, clasificación, regresión, procesamiento de lenguaje natural y muchas otras aplicaciones. 

Estas redes están compuestas por unidades llamadas "neuronas" que están interconectadas y organizadas en capas. Cada conexión entre neuronas tiene un peso que determina la fuerza de la conexión. La información fluye a través de la red desde la capa de entrada, a través de las capas ocultas (si las hay) y finalmente hacia la capa de salida. Durante este proceso, las neuronas aplican funciones de activación a la entrada ponderada para producir una salida. 

El aprendizaje en una red neuronal se logra mediante un proceso llamado retropropagación (backpropagation). Este proceso ajusta los pesos de las conexiones en función de la diferencia entre la salida predicha y la salida deseada. Se utiliza un algoritmo de optimización para minimizar esta diferencia y mejorar el rendimiento de la red. 

Existen diferentes tipos de redes neuronales, como las redes neuronales feedforward, las redes neuronales recurrentes y las redes neuronales convolucionales, cada una diseñada para abordar tipos específicos de problemas. Estas redes han demostrado ser muy efectivas en una amplia gama de aplicaciones y han contribuido significativamente al avance de la inteligencia artificial. 

Los invito a estudiar los siguientes documentos y videos: 
- Video explicativo del gradiente descendente: [Video Gradiente descendente](https://www.youtube.com/watch?v=IHZwWFHWa-w&ab_channel=3Blue1Brown3Blue1Brown)
- Este curso tiene información muy interesante alrededor del concepto de las redes neuronales: [Libro deep learning](https://atcold.github.io/pytorch-Deep-Learning/).
- Comprensión de los conceptos de redes neuronales: [Libro redes neuronales y deep learning](http://neuralnetworksanddeeplearning.com/chap1.html)
- Explicación de diferentes tipos de optimizadores: [Documento] (https://analyticsindiamag.com/ultimate-guide-to-pytorch-optimizers/)
- Explicación de diferentes funciones de error: [Documento](https://neptune.ai/blog/pytorch-loss-functions)
- Explicación de diferentes tipos de funciones de activación: [Documento[(https://towardsdatascience.com/everything-you-need-to-know-about-activation-functions-in-deep-learning-models-84ba9f82c253#:~:text=Simply%20put%2C%20an%20activation%20function,fired%20to%20the%20next%20neuron). Las diferentes funciones de activación disponibles las encontramos en el siguiente enlace: [Documento](https://machinelearningmastery.com/activation-functions-in-pytorch/)
- Un documento que explica los optimizadores SGD y ADAM: [Documento](https://machinelearningmastery.com/using-optimizers-from-pytorch/)  

Ejemplos funcionales de redes neuronales: 

- Ejemplo más avanzado, comparando varios modelos para hacer una clasificación: [Libro 6](./libro6.ipynb)
- Ejemplo de red neuronal para detectar dígitos: [Libro 7](./libro7.ipynb)


REVISAR UBICACIÓN: GPU vs CPU: Cómo el uso de la GPU acelera el trabajo de las redes neuronales: [Video: ](https://www.youtube.com/watch?v=OBxUEv6JZ-M)

Ejemplo del modelo sin GPU: [Libro modelo con CPU](./modelo_cpu.ipynb). 
Ejemplo del modelo con GPU: [Libro modelo con GPU](./modelo_gpu.ipynb)

REVISAR: Conexión a Drive, carga y descarga de un modelo 



## Redes neuronales básicas

Las redes neuronales constituyen uno de los modelos más importantes del aprendizaje automático moderno. Su objetivo es aprender relaciones complejas entre variables a partir de ejemplos, ajustando automáticamente un conjunto de parámetros internos denominados pesos.

Inspiradas de manera simplificada en el funcionamiento del cerebro humano, las redes neuronales están formadas por unidades de procesamiento interconectadas llamadas neuronas artificiales. Al combinar múltiples neuronas y capas, estas redes son capaces de aproximar funciones altamente complejas y resolver problemas de clasificación, regresión, visión por computador y procesamiento de lenguaje natural.

---

## Neurona artificial

La neurona artificial es la unidad básica de una red neuronal. Su función es recibir un conjunto de entradas, combinarlas mediante parámetros ajustables y producir una salida.

Conceptualmente, una neurona puede entenderse como un sistema que:

1. recibe información de entrada,
2. asigna una importancia a cada entrada,
3. combina la información,
4. produce una respuesta.

Matemáticamente, una neurona realiza una transformación del tipo:

```math
z = W X + b
```

donde:

- \(X\) representa las variables de entrada;
- \(W\) representa los pesos o parámetros del modelo;
- \(b\) representa el sesgo (*bias*);
- \(z\) es la salida lineal de la neurona.

Posteriormente, esta salida suele transformarse mediante una función de activación para introducir no linealidad:

```math
y = f(z)
```

donde \(f\) es una función de activación como ReLU o Sigmoid.

---

## Capas lineales

Una capa lineal es un conjunto de neuronas que aplican simultáneamente transformaciones lineales sobre las entradas.

La operación fundamental de una capa lineal es:

```math
Y = W X + B
```

o, de forma más general para múltiples observaciones:

```math
Y = XW^T + B
```

donde:

- \(X\) es el tensor de entrada;
- \(W\) es la matriz de pesos;
- \(B\) es el vector de sesgos;
- \(Y\) es la salida de la capa.

---

### Los pesos \(W\)

Los pesos representan la importancia que la red asigna a cada variable de entrada.

Por ejemplo, si una neurona recibe dos entradas:

```math
x_1 \quad \text{y} \quad x_2
```

la salida podría calcularse como:

```math
z = w_1 x_1 + w_2 x_2 + b
```

Si:

```math
w_1 > w_2
```

entonces la primera variable tiene una mayor influencia sobre la salida.

Durante el entrenamiento, el algoritmo ajusta automáticamente estos pesos para minimizar el error del modelo.

---

### El sesgo \(B\)

El sesgo o *bias* permite desplazar la función aprendida.

Sin el sesgo, todas las transformaciones lineales pasarían obligatoriamente por el origen.

El sesgo aumenta la flexibilidad del modelo y le permite representar relaciones más complejas entre las variables.

---

### Implementación en PyTorch

En PyTorch, una capa lineal se implementa mediante:

```python
import torch.nn as nn

capa = nn.Linear(
    in_features=10,
    out_features=5
)
```

donde:

- `in_features` indica el número de variables de entrada;
- `out_features` indica el número de neuronas de salida.

Internamente, PyTorch crea automáticamente:

```text
W: (5 × 10)
B: (5)
```

y aprende sus valores durante el entrenamiento.

---

## Redes secuenciales

Una red neuronal profunda se construye combinando múltiples capas una después de otra.

La salida de una capa se convierte en la entrada de la siguiente:

```text
Entrada
   ↓
Capa Lineal
   ↓
Activación
   ↓
Capa Lineal
   ↓
Activación
   ↓
Salida
```

Este encadenamiento de capas permite aprender representaciones progresivamente más complejas.

Por ejemplo:

- las primeras capas pueden aprender patrones simples;
- las capas intermedias pueden aprender estructuras más elaboradas;
- las capas profundas pueden aprender conceptos abstractos.

En visión por computador:

- las primeras capas detectan bordes;
- las capas intermedias detectan formas;
- las capas profundas detectan objetos completos.

---

### Funciones de activación entre capas

Las funciones de activación constituyen uno de los elementos fundamentales de las redes neuronales profundas. Su principal objetivo es introducir no linealidad dentro del modelo, permitiendo aprender relaciones complejas entre las variables.

Sin funciones de activación, una red neuronal formada por múltiples capas lineales sería equivalente a una única transformación lineal, limitando significativamente su capacidad de representación.

De manera general, una neurona calcula primero una combinación lineal:

```math
z = WX + b
```

y posteriormente aplica una función de activación:

```math
y = f(z)
```

donde \(f\) representa la función de activación.

Las funciones de activación permiten modelar fenómenos no lineales presentes en problemas reales de clasificación, regresión, visión por computador y procesamiento de lenguaje natural.

---

#### Sigmoid

La función Sigmoid fue una de las primeras funciones de activación utilizadas en redes neuronales.

Se define como:

```math
\sigma(x)=\frac{1}{1+e^{-x}}
```

Su salida se encuentra en el intervalo:

```math
(0,1)
```

por lo que puede interpretarse como una probabilidad.

Características:

- transforma cualquier valor real en un número entre 0 y 1;
- es continua y diferenciable;
- históricamente fue ampliamente utilizada en clasificación binaria.

Su forma característica es:

```text
         1 ───────────
            /
           /
          /
─────────
```

---

##### Ventajas

- Interpretación probabilística.
- Función suave y diferenciable.

##### Desventajas

- Sufre del problema del gradiente desvanecido (*vanishing gradient*).
- Para valores grandes de entrada la derivada tiende a cero.
- Actualmente se utiliza principalmente en capas de salida para clasificación binaria.

---

##### Implementación en PyTorch

```python
import torch.nn as nn

nn.Sigmoid()
```

---

#### Tanh

La función tangente hiperbólica (*Hyperbolic Tangent*) se define como:

```math
\tanh(x)=\frac{e^x-e^{-x}}{e^x+e^{-x}}
```

Su rango es:

```math
(-1,1)
```

A diferencia de Sigmoid, está centrada alrededor del cero.

---

##### Ventajas

- Produce salidas positivas y negativas.
- Facilita el entrenamiento en algunos problemas.

##### Desventajas

- También presenta gradiente desvanecido.
- Ha sido reemplazada en gran medida por ReLU.

---

##### Implementación en PyTorch

```python
nn.Tanh()
```

---

#### ReLU

La función ReLU (*Rectified Linear Unit*) es actualmente la función de activación más utilizada en Deep Learning.

Se define como:

```math
ReLU(x)=\max(0,x)
```

Esto significa que:

- los valores negativos se convierten en cero;
- los valores positivos permanecen sin modificación.

Su forma es:

```text
          /
         /
        /
───────
```

---

##### Ventajas

- Computacionalmente eficiente.
- Reduce el problema del gradiente desvanecido.
- Favorece representaciones dispersas.
- Facilita el entrenamiento de redes profundas.

---

##### Problema de neuronas muertas

Si una neurona produce valores negativos permanentemente, puede dejar de actualizarse.

Este fenómeno se conoce como:

```text
Dying ReLU
```

---

##### Implementación en PyTorch

```python
nn.ReLU()
```

---

#### Leaky ReLU

Leaky ReLU fue propuesta para mitigar el problema de las neuronas muertas.

Se define como:

```math
f(x)=
\begin{cases}
x, & x>0 \\
\alpha x, & x\le0
\end{cases}
```

donde:

```math
\alpha
```

es un pequeño valor positivo, típicamente:

```math
0.01
```

De esta manera, incluso para entradas negativas existe un pequeño gradiente.

---

##### Ventajas

- Reduce el problema de neuronas muertas.
- Mantiene gradientes distintos de cero.

##### Implementación en PyTorch

```python
nn.LeakyReLU(0.01)
```

---

#### Softmax

Softmax transforma un vector de valores reales en una distribución de probabilidad.

Dado un vector:

```math
z=(z_1,z_2,\ldots,z_n)
```

la función Softmax se define como:

```math
P_i=
\frac{e^{z_i}}
{\sum_j e^{z_j}}
```

La salida cumple:

```math
\sum_i P_i = 1
```

por lo que puede interpretarse como probabilidades sobre múltiples clases.

---

##### Ejemplo

Supóngase que un modelo produce:

```text
[2.0, 1.0, 0.1]
```

Después de aplicar Softmax:

```text
[0.66, 0.24, 0.10]
```

La primera clase tiene la mayor probabilidad.

---

##### Uso típico

Softmax se utiliza principalmente en la capa de salida de problemas de clasificación multiclase.

---

##### Implementación en PyTorch

```python
nn.Softmax(dim=1)
```

---

#### Comparación de funciones de activación

| Función | Rango | Uso típico |
|---------|------|------------|
| Sigmoid | (0,1) | Clasificación binaria |
| Tanh | (-1,1) | Redes clásicas |
| ReLU | [0,\infty) | Capas ocultas |
| Leaky ReLU | (-\infty,\infty) | Capas ocultas |
| Softmax | Probabilidades | Clasificación multiclase |

---

### Redes secuenciales en PyTorch

PyTorch proporciona el módulo `nn.Sequential`, que permite construir redes mediante la composición de capas:

```python
modelo = nn.Sequential(
    nn.Linear(10, 32),
    nn.ReLU(),
    nn.Linear(32, 16),
    nn.ReLU(),
    nn.Linear(16, 2)
)
```

En este ejemplo:

1. la entrada posee 10 características;
2. la primera capa produce 32 salidas;
3. se aplica una activación ReLU;
4. la segunda capa produce 16 salidas;
5. la última capa genera dos valores de salida.

Las redes secuenciales son especialmente útiles para construir modelos sencillos y constituyen un excelente punto de partida para comprender arquitecturas más complejas como CNNs y Transformers.

En realidad existen dos formas de crear el modelo. Por medio del contenedor Sequential o por la declaración de una clase y su instancia

Forma basada en clases:  
```python
import torch 
import torch.nn as nn 
class MLP(nn.Module): 
    def __init__(self, input_dim=10, hidden_dim=32, output_dim=3): 
        super().__init__() 
        self.fc1 = nn.Linear(input_dim, hidden_dim) 
        self.fc2 = nn.Linear(hidden_dim, 16) 
        self.fc3 = nn.Linear(16, output_dim) 
        self.relu = nn.ReLU() 

    def forward(self, x): 
        x = self.relu(self.fc1(x)) 
        x = self.relu(self.fc2(x)) 
        x = self.fc3(x)   # logits 
        return x 

#Instancia del modelo 
model_custom = MLP() 
#Ejemplo de uso 
x = torch.randn(8, 10) 
y = model_custom(x) 
```

---

## Aprendizaje en redes neuronales

Durante el entrenamiento, la red ajusta automáticamente sus pesos y sesgos para minimizar una función de pérdida.

El ciclo básico de aprendizaje es:

```text
Datos
    ↓
Red neuronal
    ↓
Predicción
    ↓
Error
    ↓
Gradientes
    ↓
Actualización de pesos
```

A través de miles o millones de iteraciones, la red aprende representaciones internas cada vez más útiles para resolver la tarea planteada.




### Aprendizaje supervisado

El aprendizaje supervisado es uno de los paradigmas fundamentales del Machine Learning y Deep Learning.

En este enfoque, el modelo aprende a partir de ejemplos etiquetados:

```text
Entrada → Salida esperada
```

Por ejemplo:

| Imagen | Clase |
|--------|------|
| Gato | 0 |
| Perro | 1 |

El objetivo es aprender una función:

```math
f(X)\approx Y
```

que permita predecir correctamente nuevas observaciones.

---
#### Funciones de pérdida

Para aprender, la red necesita medir qué tan buena o mala es una predicción.

Las funciones de pérdida (*loss functions*) cuantifican el error entre la salida del modelo y el valor esperado.

Formalmente:

```math
L(y,\hat y)
```

donde:

- \(y\) es el valor verdadero;
- \(\hat y\) es la predicción del modelo.

El objetivo del entrenamiento es minimizar esta pérdida.

---

#### Error Cuadrático Medio (MSE)

El Error Cuadrático Medio (*Mean Squared Error*) es ampliamente utilizado en problemas de regresión.

Se define como:

```math
MSE=
\frac{1}{N}
\sum_{i=1}^N
(y_i-\hat y_i)^2
```

El error se eleva al cuadrado para:

- penalizar errores grandes;
- garantizar positividad;
- facilitar la optimización.

---

##### Aplicaciones

- Predicción de precios.
- Pronóstico de demanda.
- Estimación de variables continuas.

---

##### Implementación en PyTorch

```python
criterion = nn.MSELoss()
```

---

#### Cross Entropy

La entropía cruzada (*Cross Entropy*) es la función de pérdida más utilizada en clasificación.

Mide la diferencia entre:

- la distribución real;
- la distribución predicha por el modelo.

Para clasificación multiclase:

```math
L=
-\sum_i y_i \log(\hat y_i)
```

La pérdida es pequeña cuando el modelo asigna alta probabilidad a la clase correcta.

---

##### Ejemplo

Clase verdadera:

```text
[1,0,0]
```

Predicción:

```text
[0.90,0.08,0.02]
```

produce una pérdida pequeña.

Pero:

```text
[0.10,0.70,0.20]
```

produce una pérdida grande.

---

##### Implementación en PyTorch

```python
criterion = nn.CrossEntropyLoss()
```

Esta función incorpora internamente Softmax, por lo que generalmente no debe aplicarse Softmax antes de la pérdida.

---

#### Optimización

Una vez calculada la pérdida, el modelo debe ajustar sus parámetros para reducir el error.

Este proceso se realiza mediante algoritmos de optimización.

El más básico es el descenso de gradiente:

```math
\theta_{t+1}
=
\theta_t
-
\eta
\nabla L
```

donde:

- \(\theta\) representa los parámetros;
- \(\eta\) es la tasa de aprendizaje (*learning rate*);
- \(\nabla L\) es el gradiente de la pérdida.

---

##### Algoritmos comunes

##### SGD (*Stochastic Gradient Descent*)

El descenso de gradiente estocástico (**Stochastic Gradient Descent**, SGD) es uno de los algoritmos de optimización más fundamentales en aprendizaje automático y constituye la base conceptual de muchos optimizadores modernos.

La idea central consiste en actualizar los parámetros del modelo en dirección opuesta al gradiente de la función de pérdida:

```math
\theta_{t+1}
=
\theta_t
-
\eta
\nabla L
```

donde:

- \(\theta_t\) representa los parámetros actuales;
- \(\eta\) es la tasa de aprendizaje (*learning rate*);
- \(\nabla L\) es el gradiente de la pérdida.

El término "estocástico" se refiere a que los gradientes se calculan utilizando un lote (*batch*) de observaciones y no necesariamente el conjunto completo de datos.

---

###### Ventajas

- Conceptualmente simple.
- Bajo consumo de memoria.
- Buena capacidad de generalización.
- Amplio respaldo teórico.

###### Desventajas

- Puede converger lentamente.
- Es sensible a la elección de la tasa de aprendizaje.
- Puede oscilar cerca del mínimo.

---

###### Momentum

En la práctica, SGD suele utilizarse junto con un mecanismo denominado **momentum**, que acumula información de gradientes anteriores para acelerar el entrenamiento:

```python
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01,
    momentum=0.9
)
```

---

###### Uso típico

SGD es ampliamente utilizado cuando:

- se dispone de grandes cantidades de datos;
- se desea una mejor capacidad de generalización;
- se entrenan modelos de visión por computador.

En particular, muchos modelos de clasificación de imágenes sobre ImageNet han sido entrenados utilizando SGD con momentum.

---

##### Adam

**Adam** (*Adaptive Moment Estimation*) es uno de los optimizadores más utilizados actualmente en Deep Learning.

Adam combina dos ideas fundamentales:

1. Momentum: suaviza las actualizaciones utilizando gradientes pasados.
2. Tasas de aprendizaje adaptativas: ajusta automáticamente el tamaño del paso para cada parámetro.

Esto permite un entrenamiento más rápido y estable.

---

###### Intuición

Mientras SGD utiliza una única tasa de aprendizaje para todos los parámetros:

```text
Todos los pesos → misma tasa de aprendizaje
```

Adam ajusta automáticamente la tasa de aprendizaje de cada parámetro:

```text
Peso 1 → aprendizaje rápido
Peso 2 → aprendizaje lento
Peso 3 → aprendizaje intermedio
```

Esto resulta especialmente útil en modelos con millones de parámetros.

---

###### Ventajas

- Generalmente converge más rápido.
- Requiere menos ajuste manual.
- Funciona bien en una gran variedad de problemas.
- Es robusto ante gradientes ruidosos.

###### Desventajas

- Puede presentar peor generalización que SGD en algunos casos.
- Puede converger a soluciones menos óptimas.

---

###### Implementación en PyTorch

```python
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)
```

---

###### Uso típico

Adam es una excelente primera opción para:

- redes neuronales profundas;
- procesamiento de lenguaje natural;
- Transformers;
- LLMs;
- experimentación rápida.

Por esta razón, gran parte de los modelos modernos basados en Transformers utilizan variantes de Adam.

---

##### RMSProp

**RMSProp** (*Root Mean Square Propagation*) fue propuesto para resolver problemas asociados a gradientes con escalas muy diferentes.

La idea fundamental es adaptar la tasa de aprendizaje utilizando un promedio móvil de los gradientes al cuadrado.

Como resultado:

- parámetros con gradientes grandes reciben actualizaciones más pequeñas;
- parámetros con gradientes pequeños reciben actualizaciones mayores.

Esto estabiliza el entrenamiento.

---

###### Ventajas

- Maneja adecuadamente gradientes ruidosos.
- Funciona bien en problemas secuenciales.
- Mejora la estabilidad del entrenamiento.

###### Desventajas

- Ha sido ampliamente reemplazado por Adam.
- Posee más hiperparámetros que SGD.

---

###### Implementación en PyTorch

```python
optimizer = torch.optim.RMSprop(
    model.parameters(),
    lr=0.001
)
```

---

###### Uso típico

RMSProp ha sido históricamente utilizado en:

- redes recurrentes (RNN);
- procesamiento secuencial;
- aprendizaje por refuerzo.

Aunque hoy en día Adam suele ser la alternativa preferida, RMSProp sigue apareciendo en algunos algoritmos clásicos de Reinforcement Learning.

---

##### AdamW

**AdamW** es una mejora sobre Adam diseñada para manejar adecuadamente la regularización mediante **Weight Decay**.

Aunque Adam permite incluir el parámetro:

```text
weight_decay
```

investigaciones posteriores mostraron que la implementación original no realizaba una separación correcta entre:

- optimización;
- regularización.

AdamW desacopla explícitamente ambos procesos, produciendo una regularización más efectiva.

---

###### Ventajas

- Mejor regularización que Adam.
- Reduce el riesgo de overfitting.
- Es el optimizador estándar en Transformers modernos.

###### Desventajas

- Requiere ajustar el parámetro `weight_decay`.
- Su comportamiento es similar a Adam en problemas pequeños.

---

###### Implementación en PyTorch

```python
optimizer = torch.optim.AdamW(
    model.parameters(),
    lr=0.001,
    weight_decay=1e-4
)
```

---

###### Uso típico

AdamW es actualmente el optimizador recomendado para:

- Transformers;
- BERT;
- GPT;
- modelos multimodales;
- sistemas RAG;
- grandes modelos de lenguaje.

De hecho, gran parte de los LLM modernos utilizan AdamW o variantes derivadas.

---

##### Comparación de optimizadores

| Optimizador | Velocidad | Generalización | Uso típico |
|-------------|-----------|----------------|------------|
| SGD | Media | Excelente | Visión por computador |
| Adam | Alta | Buena | Deep Learning general |
| RMSProp | Alta | Buena | RNN y RL |
| AdamW | Alta | Muy buena | Transformers y LLMs |

No existe un optimizador universalmente mejor. La elección depende del problema, la arquitectura y el tamaño del conjunto de datos. Sin embargo, como regla general:

- **SGD** suele ser una excelente elección para visión por computador.
- **Adam** es una buena primera opción para prototipos.
- **AdamW** es el estándar actual para Transformers y LLMs.
Actualmente, Adam es uno de los optimizadores más utilizados debido a su estabilidad y velocidad de convergencia.

---

##### Implementación en PyTorch

```python
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)
```

---

#### Ciclo de entrenamiento supervisado

El proceso completo de aprendizaje puede resumirse como:

```text
Datos
   ↓
Modelo
   ↓
Predicción
   ↓
Función de pérdida
   ↓
Gradientes (Autograd)
   ↓
Optimizador
   ↓
Actualización de pesos
```

Este ciclo se repite durante múltiples épocas hasta que el modelo alcanza un desempeño adecuado sobre datos no observados previamente.


#### Descenso de gradiente

El objetivo del entrenamiento de una red neuronal es encontrar un conjunto de parámetros (pesos y sesgos) que permitan realizar predicciones precisas sobre datos no observados previamente.

Este proceso se formula como un problema de optimización: minimizar una función de pérdida ajustando iterativamente los parámetros del modelo.

El algoritmo más utilizado para este propósito es el **descenso de gradiente** (*Gradient Descent*).

---

##### Forward pass

El *forward pass* corresponde al proceso mediante el cual los datos atraviesan la red neuronal para generar una predicción.

Durante esta etapa:

1. Los datos de entrada son suministrados al modelo.
2. Cada capa realiza transformaciones lineales.
3. Se aplican funciones de activación.
4. Se obtiene una salida o predicción.

Por ejemplo:

```text
Datos
   ↓
Capa lineal
   ↓
ReLU
   ↓
Capa lineal
   ↓
Softmax
   ↓
Predicción
```

Formalmente, si una red neuronal implementa una función:

```math
\hat y = f(X;\theta)
```

donde:

- \(X\) representa las entradas;
- \(\theta\) representa los parámetros del modelo;
- \(\hat y\) corresponde a la predicción.

El resultado del *forward pass* se utiliza posteriormente para calcular la función de pérdida.

---

###### Ejemplo en PyTorch

```python
y_pred = model(X)
loss = criterion(y_pred, y)
```

donde:

- `model(X)` realiza el forward pass;
- `criterion` calcula la pérdida.

---

##### Backpropagation

Una vez calculado el error, la red neuronal debe determinar cómo modificar cada uno de sus parámetros para reducir dicho error.

Este proceso se denomina **backpropagation** o propagación hacia atrás.

La idea fundamental es calcular el gradiente de la función de pérdida respecto a cada parámetro:

```math
\frac{\partial L}{\partial \theta}
```

Estos gradientes indican:

- la dirección en la que debe modificarse cada parámetro;
- la magnitud del cambio necesario.

---

###### Regla de la cadena

El algoritmo de backpropagation utiliza la regla de la cadena del cálculo diferencial para propagar gradientes desde la salida de la red hasta sus capas más profundas.

Conceptualmente:

```text
Salida
   ↑
Gradientes
   ↑
Capas profundas
   ↑
Capas iniciales
```

PyTorch realiza este proceso automáticamente mediante el sistema `Autograd`.

---

###### Cálculo automático de gradientes

```python
loss.backward()
```

La instrucción anterior:

1. recorre el grafo computacional;
2. calcula derivadas parciales;
3. almacena los gradientes en cada parámetro del modelo.

Por ejemplo:

```python
for p in model.parameters():
    print(p.grad)
```

permite inspeccionar los gradientes calculados.

---

##### Actualización de pesos

Una vez calculados los gradientes, el optimizador actualiza los parámetros del modelo.

La actualización básica del descenso de gradiente es:

```math
\theta_{t+1}
=
\theta_t
-
\eta
\nabla L
```

donde:

- \(\theta_t\) son los parámetros actuales;
- \(\eta\) es la tasa de aprendizaje (*learning rate*);
- \(\nabla L\) representa el gradiente.

El objetivo es mover los parámetros en la dirección que reduce la pérdida.

---

###### Tasa de aprendizaje

La tasa de aprendizaje controla el tamaño de cada actualización.

Si es muy grande:

- el entrenamiento puede volverse inestable;
- el modelo puede no converger.

Si es muy pequeña:

- el entrenamiento será lento;
- el modelo puede quedar atrapado en mínimos locales.

Valores comunes son:

```text
0.1
0.01
0.001
```

---

###### Actualización en PyTorch

El ciclo básico es:

```python
optimizer.zero_grad()

y_pred = model(X)

loss = criterion(y_pred, y)

loss.backward()

optimizer.step()
```

donde:

- `zero_grad()` elimina gradientes previos;
- `backward()` calcula gradientes;
- `step()` actualiza los parámetros.

---

#### Ciclo completo de aprendizaje

```text
Datos
   ↓
Forward pass
   ↓
Predicción
   ↓
Función de pérdida
   ↓
Backpropagation
   ↓
Gradientes
   ↓
Actualización de pesos
```

Este ciclo se repite durante múltiples épocas hasta alcanzar un desempeño satisfactorio.

---

#### Gestión de datos

En Deep Learning, el rendimiento de un modelo no depende únicamente de la arquitectura de la red neuronal. La forma en que se organizan y suministran los datos tiene un impacto fundamental sobre la velocidad, estabilidad y capacidad de generalización del entrenamiento.

PyTorch proporciona herramientas específicas para gestionar grandes conjuntos de datos de manera eficiente.

---

##### Dataset

Un `Dataset` representa una colección de observaciones y define cómo acceder a ellas.

Conceptualmente, un Dataset responde dos preguntas:

1. ¿Cuántos ejemplos existen?
2. ¿Cómo se obtiene cada ejemplo?

En PyTorch, un Dataset implementa típicamente dos métodos:

```python
__len__()
__getitem__()
```

donde:

- `__len__()` retorna el número de observaciones;
- `__getitem__(i)` retorna el ejemplo número `i`.

---

###### Ejemplo conceptual

```python
imagen, etiqueta = dataset[0]
```

En este caso:

- `imagen` contiene las variables de entrada;
- `etiqueta` contiene la salida esperada.

---

###### Datasets incorporados

PyTorch proporciona numerosos datasets predefinidos:

- MNIST
- CIFAR-10
- ImageNet
- Fashion-MNIST

Por ejemplo:

```python
from torchvision.datasets import MNIST
```

---

##### DataLoader

Aunque un Dataset permite acceder a datos individuales, durante el entrenamiento resulta más eficiente procesar múltiples observaciones simultáneamente.

Para ello se utiliza un `DataLoader`.

El DataLoader automatiza:

- creación de lotes (*batches*);
- aleatorización;
- paralelización de carga;
- iteración durante el entrenamiento.

---

###### Ejemplo

```python
from torch.utils.data import DataLoader

loader = DataLoader(
    dataset,
    batch_size=64,
    shuffle=True
)
```

Durante el entrenamiento:

```python
for X, y in loader:
    ...
```

PyTorch suministra automáticamente lotes de datos.

---

##### Batching

En Deep Learning rara vez se entrena utilizando una sola observación a la vez.

En su lugar, se procesan pequeños grupos de ejemplos denominados **batches**.

Por ejemplo:

```text
batch_size = 64
```

indica que el modelo procesa 64 observaciones simultáneamente.

---

###### Ventajas del batching

- Aprovecha el paralelismo de la GPU.
- Reduce ruido en el gradiente.
- Acelera el entrenamiento.
- Optimiza el uso de memoria.

---

###### Ejemplo de dimensiones

Si cada imagen posee forma:

```text
(3, 224, 224)
```

un batch de 64 imágenes tendrá forma:

```text
(64, 3, 224, 224)
```

La primera dimensión corresponde siempre al tamaño del lote.

---

##### Shuffle

Durante el entrenamiento es recomendable presentar los datos en orden aleatorio.

Esto evita que el modelo aprenda patrones artificiales asociados al orden de los datos.

Por ejemplo:

```text
Gato
Gato
Gato
Perro
Perro
Perro
```

podría inducir sesgos no deseados.

Con:

```python
shuffle=True
```

PyTorch reorganiza aleatoriamente las observaciones al inicio de cada época.

---

###### Beneficios del shuffle

- Mejora la generalización.
- Reduce sesgos.
- Favorece convergencia estable.

---

##### Validación

Uno de los objetivos principales del aprendizaje automático es generalizar a datos no observados.

Por esta razón, los datos suelen dividirse en tres conjuntos:

| Conjunto | Propósito |
|----------|-----------|
| Entrenamiento | Ajustar parámetros |
| Validación | Seleccionar hiperparámetros |
| Prueba | Evaluación final |

---

###### Entrenamiento

El conjunto de entrenamiento se utiliza para ajustar los pesos del modelo.

---

###### Validación

El conjunto de validación permite monitorear el desempeño durante el entrenamiento y detectar fenómenos como:

- overfitting;
- underfitting.

La validación ayuda a decidir:

- número de épocas;
- arquitectura;
- tasa de aprendizaje;
- regularización.

---

###### Conjunto de prueba

El conjunto de prueba debe utilizarse únicamente al finalizar el desarrollo del modelo.

Su objetivo es estimar el desempeño esperado sobre datos futuros.

---

###### División típica

Una partición común es:

```text
70% Entrenamiento
15% Validación
15% Prueba
```

aunque las proporciones pueden variar según el tamaño del dataset.

---

##### Pipeline completo de datos

El flujo típico de gestión de datos en PyTorch es:

```text
Dataset
   ↓
DataLoader
   ↓
Batching
   ↓
Shuffle
   ↓
Entrenamiento
   ↓
Validación
   ↓
Prueba
```

Una adecuada gestión de datos es tan importante como la arquitectura del modelo y constituye una de las bases fundamentales de los sistemas modernos de Deep Learning.

## Generalización

Uno de los principales objetivos del aprendizaje automático es construir modelos capaces de realizar buenas predicciones sobre datos que no han sido observados durante el entrenamiento.

Esta capacidad se denomina **generalización**.

Un modelo que generaliza adecuadamente ha aprendido patrones reales presentes en los datos y no simplemente ha memorizado los ejemplos de entrenamiento.

La generalización constituye uno de los problemas centrales del Deep Learning y está estrechamente relacionada con el equilibrio entre la complejidad del modelo y la cantidad de datos disponibles.

---

### Error de entrenamiento y error de validación

Para evaluar la capacidad de generalización de un modelo, normalmente se monitorean dos métricas:

- **Error de entrenamiento:** desempeño sobre los datos utilizados para ajustar los parámetros.
- **Error de validación:** desempeño sobre datos no observados durante el entrenamiento.

Idealmente, ambos errores deberían ser pequeños y similares.

Sin embargo, esto no siempre ocurre.

---

### El compromiso sesgo-varianza

La generalización puede interpretarse como un equilibrio entre dos extremos:

- modelos demasiado simples;
- modelos excesivamente complejos.

Este compromiso suele denominarse:

```text
Bias-Variance Tradeoff
```

y da origen a dos problemas fundamentales:

- Underfitting.
- Overfitting.

---

### Underfitting

El **underfitting** ocurre cuando el modelo es demasiado simple para capturar los patrones presentes en los datos.

En este caso, el modelo presenta un mal desempeño tanto en entrenamiento como en validación.

Conceptualmente:

```text
Error entrenamiento: alto
Error validación: alto
```

---

#### Causas comunes

- Pocas neuronas o capas.
- Entrenamiento insuficiente.
- Variables poco informativas.
- Modelo demasiado restrictivo.
- Regularización excesiva.

---

#### Ejemplo intuitivo

Intentar ajustar una línea recta a datos altamente no lineales:

```text
Datos complejos
      *
   *      *
 *           *
-------------------
    línea recta
```

El modelo no posee suficiente capacidad para representar la estructura de los datos.

---

#### Cómo reducir el underfitting

- Incrementar la capacidad del modelo.
- Entrenar durante más épocas.
- Incorporar mejores variables.
- Reducir regularización.

---

### Overfitting

El **overfitting** ocurre cuando el modelo aprende demasiado bien los datos de entrenamiento, incluyendo ruido o patrones accidentales que no generalizan.

En este caso:

```text
Error entrenamiento: bajo
Error validación: alto
```

El modelo memoriza en lugar de aprender.

---

#### Ejemplo intuitivo

Un estudiante memoriza exactamente los ejercicios del libro pero fracasa ante preguntas nuevas.

De forma análoga, un modelo sobreajustado funciona muy bien sobre los datos conocidos pero falla en datos futuros.

---

#### Representación gráfica

```text
Error
  ^
  |
  | \ entrenamiento
  |  \
  |   \
  |    \____
  |
  |      \ validación
  |       \
  |        \______
  +--------------------> Épocas
```

Inicialmente ambos errores disminuyen.

Sin embargo, a partir de cierto punto:

- el error de entrenamiento continúa disminuyendo;
- el error de validación comienza a aumentar.

Ese es el inicio del overfitting.

Modelo que presenta un proceso de earlyStop para controlar el overfitting [Libro de overfitting](./ejemplo_con_early_stop.ipynb)

---

#### Causas comunes

- Modelos excesivamente complejos.
- Pocos datos de entrenamiento.
- Entrenamiento demasiado prolongado.
- Ausencia de regularización.

---

#### Cómo reducir el overfitting

- Recolectar más datos.
- Aplicar regularización.
- Utilizar Dropout.
- Emplear Early Stopping.
- Aplicar Data Augmentation.
- Reducir la complejidad del modelo.

---

### Early Stopping

El **Early Stopping** es una técnica que detiene automáticamente el entrenamiento cuando el desempeño sobre el conjunto de validación deja de mejorar.

La idea es evitar que el modelo continúe aprendiendo ruido presente en los datos de entrenamiento.

---

#### Funcionamiento

Durante el entrenamiento se monitorea una métrica de validación:

```text
Pérdida de validación
```

Si dicha métrica no mejora durante varias épocas consecutivas, el entrenamiento se detiene.

Por ejemplo:

```text
Época 15: mejora
Época 16: mejora
Época 17: sin mejora
Época 18: sin mejora
Época 19: sin mejora
→ detener entrenamiento
```

---

#### Paciencia (*patience*)

El parámetro más importante es:

```text
patience
```

que indica cuántas épocas consecutivas sin mejora se permiten antes de detener el entrenamiento.

Valores comunes:

```text
5
10
20
```

---

#### Ventajas

- Reduce overfitting.
- Disminuye tiempo de entrenamiento.
- Selecciona automáticamente el mejor modelo.

---

#### Flujo conceptual

```text
Entrenamiento
      ↓
Validación
      ↓
¿Mejora?
   /     \
 Sí      No
 |        |
Continuar Contador +1
             |
      ¿Supera patience?
             |
            Sí
             ↓
        Detener
```

---

### Dropout

El **Dropout** es una técnica de regularización ampliamente utilizada en Deep Learning.

Su idea principal consiste en desactivar aleatoriamente algunas neuronas durante el entrenamiento.

De esta forma, la red no puede depender excesivamente de un conjunto reducido de neuronas y aprende representaciones más robustas.

---

#### Ejemplo conceptual

Red completa:

```text
○──○──○
│  │  │
○──○──○
│  │  │
○──○──○
```

Con Dropout:

```text
○──X──○
│     │
X──○──○
│
○──X──○
```

Las neuronas marcadas con **X** son ignoradas temporalmente.

---

#### Probabilidad de Dropout

Generalmente se especifica una probabilidad:

```text
p = 0.5
```

lo que significa que aproximadamente el 50% de las neuronas serán desactivadas en cada iteración.

Valores comunes:

```text
0.1
0.2
0.5
```

---

#### Entrenamiento vs inferencia

Es importante notar que:

- durante el entrenamiento, Dropout está activo;
- durante la inferencia, todas las neuronas participan.

PyTorch gestiona este comportamiento automáticamente mediante:

```python
model.train()
model.eval()
```

---

#### Implementación en PyTorch

```python
nn.Dropout(p=0.5)
```

---

### Weight Decay

El **Weight Decay** es una técnica de regularización que penaliza pesos excesivamente grandes.

La idea es que modelos más simples tienden a generalizar mejor.

Para ello se agrega un término adicional a la función de pérdida:

```math
L_{total}
=
L
+
\lambda ||W||^2
```

donde:

- \(L\) es la pérdida original;
- \(W\) representa los pesos del modelo;
- \(\lambda\) controla la intensidad de la penalización.

Esta técnica también es conocida como:

```text
Regularización L2
```

---

#### Interpretación intuitiva

Sin regularización:

```text
pesos muy grandes
→ modelos complejos
→ riesgo de overfitting
```

Con Weight Decay:

```text
pesos moderados
→ modelos más simples
→ mejor generalización
```

---

#### Implementación en PyTorch

```python
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001,
    weight_decay=1e-4
)
```

El optimizador incorpora automáticamente la penalización durante el entrenamiento.

---

### Estrategias modernas de generalización

En la práctica, los modelos modernos suelen combinar múltiples técnicas simultáneamente:

- División entrenamiento/validación/prueba.
- Early Stopping.
- Dropout.
- Weight Decay.
- Data Augmentation.
- Transfer Learning.

El objetivo final es construir modelos que no solo aprendan los datos disponibles, sino que también sean capaces de responder adecuadamente ante nuevas situaciones.

---

### Resumen

| Problema o técnica | Objetivo |
|-------------------|----------|
| Underfitting | Incrementar capacidad del modelo |
| Overfitting | Reducir memorización |
| Early Stopping | Detener entrenamiento oportunamente |
| Dropout | Robustecer representaciones internas |
| Weight Decay | Penalizar modelos demasiado complejos |

La generalización constituye uno de los principios más importantes del aprendizaje profundo, ya que el verdadero valor de un modelo no radica en memorizar el pasado, sino en predecir correctamente el futuro.

## Pipeline completo

REVISAR: Red neuronal aplicada en dos problemas de clasificación: [Libro de problemas de clasificación](./libro5.ipynb)

Hasta este punto hemos estudiado múltiples conceptos: tensores, redes neuronales, funciones de activación, funciones de pérdida, optimización y gestión de datos. Sin embargo, uno de los objetivos centrales de este curso es comprender que el desarrollo de sistemas modernos de Inteligencia Artificial no se basa únicamente en modelos, sino en **pipelines completos de procesamiento de datos**.

En la práctica, una red neuronal es solo uno de los componentes de un sistema más amplio. El verdadero valor surge cuando múltiples etapas trabajan conjuntamente para transformar datos crudos en predicciones o decisiones útiles.

Por ello, resulta más apropiado pensar en términos de un **pipeline de aprendizaje profundo** que en términos de modelos aislados.

El flujo general puede representarse como:

```text
Datos
   ↓
Dataset
   ↓
DataLoader
   ↓
Modelo
   ↓
Función de pérdida
   ↓
Optimizador
   ↓
Entrenamiento
   ↓
Evaluación
   ↓
Inferencia
```

Cada uno de estos componentes cumple una función específica dentro del sistema.

---

### Datos

Todo sistema de aprendizaje automático comienza con datos.

Dependiendo del problema, estos pueden corresponder a:

- imágenes,
- documentos,
- audio,
- video,
- sensores,
- registros transaccionales.

Los datos constituyen la materia prima a partir de la cual el modelo aprenderá patrones.

Por ejemplo:

```text
Imágenes de radiografías
Etiquetas: sano / enfermedad
```

o

```text
Documentos legales
Etiquetas: tipo de contrato
```

La calidad y cantidad de los datos suelen ser más importantes que la complejidad del modelo utilizado.

---

### Dataset

Los datos crudos raramente se utilizan directamente.

Es necesario construir una interfaz que permita:

- acceder a cada observación;
- cargar archivos desde disco;
- aplicar transformaciones;
- retornar entradas y salidas.

Esta tarea es realizada por el objeto `Dataset`.

Conceptualmente:

```text
Archivo → Transformación → Tensor
```

Por ejemplo, un Dataset de imágenes puede:

1. leer una imagen del disco;
2. redimensionarla;
3. normalizarla;
4. convertirla en un tensor;
5. retornar su etiqueta.

En PyTorch:

```python
imagen, etiqueta = dataset[i]
```

---

### DataLoader

Aunque el Dataset permite acceder a ejemplos individuales, el entrenamiento eficiente requiere procesar múltiples observaciones simultáneamente.

El `DataLoader` automatiza:

- creación de lotes (*batches*);
- aleatorización;
- carga paralela;
- iteración sobre el dataset.

Por ejemplo:

```python
loader = DataLoader(
    dataset,
    batch_size=64,
    shuffle=True
)
```

Durante el entrenamiento:

```python
for X, y in loader:
    ...
```

el DataLoader suministra automáticamente lotes de datos listos para el modelo.

---

### Modelo

El modelo representa la función matemática que aprenderá a transformar las entradas en salidas.

Por ejemplo:

```text
Imagen → Clase
Texto → Sentimiento
Audio → Transcripción
```

En PyTorch, un modelo puede implementarse mediante:

```python
model = nn.Sequential(
    nn.Linear(100, 64),
    nn.ReLU(),
    nn.Linear(64, 10)
)
```

Es importante notar que el modelo es únicamente un componente del pipeline y no el sistema completo.

---

### Función de pérdida

Una vez generada una predicción, el sistema necesita medir qué tan buena o mala es.

La función de pérdida cuantifica el error entre:

```text
Predicción
vs
Valor real
```

Por ejemplo:

- MSE para regresión;
- Cross Entropy para clasificación.

La pérdida constituye la señal que guía el aprendizaje.

---

### Optimizador

El optimizador utiliza los gradientes calculados por Autograd para actualizar los parámetros del modelo.

Su función es responder la pregunta:

> ¿Cómo deben modificarse los pesos para reducir el error?

Entre los optimizadores más utilizados se encuentran:

- SGD;
- Adam;
- AdamW.

En PyTorch:

```python
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)
```

---

### Entrenamiento

Durante el entrenamiento, el sistema repite iterativamente el ciclo de aprendizaje:

```text
Batch
   ↓
Forward pass
   ↓
Predicción
   ↓
Pérdida
   ↓
Backward pass
   ↓
Gradientes
   ↓
Actualización de pesos
```

Cada recorrido completo sobre el dataset recibe el nombre de **época** (*epoch*).

El entrenamiento continúa hasta que el modelo alcanza un desempeño satisfactorio o se detecta sobreentrenamiento.

---

### Evaluación

Una vez entrenado el modelo, es necesario medir su desempeño sobre datos no observados previamente.

La evaluación permite responder preguntas como:

- ¿Qué tan preciso es el modelo?
- ¿Generaliza adecuadamente?
- ¿Presenta overfitting?

Dependiendo del problema, pueden utilizarse métricas como:

- Accuracy;
- Precision;
- Recall;
- F1-score;
- Error cuadrático medio.

La evaluación constituye un componente esencial del pipeline y no debe confundirse con el entrenamiento.

---

### Inferencia

Finalmente, el sistema se utiliza para realizar predicciones sobre nuevos datos.

Este proceso se denomina **inferencia**.

Por ejemplo:

```text
Nueva imagen
   ↓
Preprocesamiento
   ↓
Modelo entrenado
   ↓
Predicción
```

Durante la inferencia:

- los pesos permanecen fijos;
- no se calculan gradientes;
- el objetivo es obtener respuestas rápidas y precisas.

En PyTorch:

```python
model.eval()

with torch.no_grad():
    y_pred = model(X)
```

---

### Del modelo al sistema

Uno de los objetivos centrales de este curso es desarrollar una visión sistémica de la Inteligencia Artificial.

En la práctica, los problemas reales rara vez consisten únicamente en entrenar un modelo. Más bien, implican construir sistemas completos capaces de transformar datos no estructurados en información útil.

Por ejemplo:

#### Analítica visual

```text
Imágenes
   ↓
Dataset
   ↓
CNN
   ↓
Clasificación
   ↓
Evaluación
   ↓
Despliegue
```

#### Procesamiento de lenguaje natural

```text
Documentos
   ↓
Limpieza
   ↓
Embeddings
   ↓
Recuperación
   ↓
LLM
   ↓
Respuesta
```

#### Sistemas RAG

```text
PDFs
   ↓
Chunking
   ↓
Embeddings
   ↓
Base vectorial
   ↓
Retrieval
   ↓
LLM
   ↓
Respuesta fundamentada
```

Así, el aprendizaje profundo moderno debe entenderse no como una colección de modelos aislados, sino como la construcción de pipelines capaces de convertir datos en conocimiento y conocimiento en decisiones.


