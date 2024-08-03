import streamlit as st
import pandas as pd
import numpy as np

# Título de la aplicación
st.title('Mi Primera Aplicación con Streamlit')

# Subtítulo
st.header('Visualización de Datos de Ejemplo')

# Crear un DataFrame de ejemplo
data = pd.DataFrame({
    'Número': np.arange(1, 11),
    'Aleatorio': np.random.randn(10)
})

# Mostrar el DataFrame
st.write("Aquí hay algunos datos de ejemplo:")
st.write(data)

# Crear un gráfico de líneas con los datos
st.line_chart(data)

# Slider para seleccionar un valor
valor_seleccionado = st.slider('Selecciona un valor', 0, 10, 5)
st.write('Valor seleccionado:', valor_seleccionado)

# Crear un filtro en el DataFrame basado en el valor seleccionado
filtered_data = data[data['Número'] <= valor_seleccionado]

# Mostrar el DataFrame filtrado
st.write("Datos filtrados hasta el número seleccionado:")
st.write(filtered_data)

# Crear un gráfico de barras con los datos filtrados
st.bar_chart(filtered_data.set_index('Número'))