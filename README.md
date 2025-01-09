# Proyecto-2
le preguntas al codigo algo relacionado sobre el contexto que ponga y gracias a la fastapi este analizara la pregunta dependiendo del contexto que le hallas escrito en el codigo y te responde

se usan las librerias: transformers, FastApi de hugginface, pidantic y uvicorn

Instalacion

- Descargar el app.py
- Guardalo en un directorio
- instala las librerias del requirements.txt


Ejecucion
- Una vez el archivo app.py descargado ejecutalo en la consola si ya estan todas las librerias instaladas

![image](https://github.com/user-attachments/assets/a6122cfd-21f8-4b09-b045-2a196612bc99)


- Una vez ejecutado el codigo empezara a funcionar el servidor, para mandar la pregunta sobre el contexto que pusiste en el codigo, debes mandarlo por medio de Postman

el formato para mandar la pregunta por json es:

{
  "question": "Aqui dejas tu pregunta",
  "model_name": "distilbert-base-uncased-distilled-squad"
}

puede ser por la extension de visual studio code:

![image](https://github.com/user-attachments/assets/492c04bc-d2eb-4095-a8b9-c0130caacb6d)

o por via de un comando curl:
ejemplo: curl -X POST "aqui va la direccion de servidor que te sale al iniciar la app.py debe ir un /ask/" -H "Content-Type: application/json" -d '{"question": "¿aqui va la pregunta?", "model_name": "distilbert-base-uncased-distilled-squad"}'

ejemplo: curl -X POST "http://150.0.0.2:5000/ask/" -H "Content-Type: application/json" -d '{"question": "¿Cuál es la capital de Francia?", "model_name": "distilbert-base-uncased-distilled-squad"}'

Para cambiar el contexto que quieres que te responda debes ir al codigo y agregar un context:

![image](https://github.com/user-attachments/assets/5bc5b2d0-0720-49b6-afd1-92a7b99f331b)








