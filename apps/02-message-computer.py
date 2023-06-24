def message_creator(text):
   answers = {
      'computadora': 'Con mi computadora puedo programar usando Python',
      'celular': 'En mi celular puedo aprender usando la app de Platzi',
      'cable': '¡Hay un cable en mi bota!'
   }
   result = answers.get(text.lower())
   if not result:
      result = 'Artículo no encontrado'
   return result

text = 'computadora'
response = message_creator(text)
print(response)