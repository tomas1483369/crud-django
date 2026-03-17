//Proyecto de  Django v6.0.3//

//Requeriments//
asgiref==3.11.1
Django==6.0.3
sqlparse==0.5.5
tzdata==2025.3

//Crear entorno Virtual// 
py -m venv venv

//Activar entorno virtual//
venv\Scripts\activate

//Iniciar servidor//
python manage.py runserver

//Evitar problemas con urls/
usar esta estructura para evitar conflictos con urls y poder cambiarlas sin problemas
{% url 'aqui va el nombre que le damos a la url no la direccion' %}

//Diccionario de errores//

(404) Page no found : no se encuentra la ruta 

TemplateDoesNoExits : cuando pedimos a django mostrar una pagina y busca en todos los archivos y no la encuentra 

TemplateSyntaxError : Este es un error de sintaxis o error de ortografia o tambien puede ser logico ocurre con las etiquetas de django en el HTML

UnboundLocalError: Es cuando estas tratando de usar una variable que todavia no existe en esa parte del codigo

TypeError: es un error generico la mayoria de las veces significa que estas llamando a una funcion con los argumentos equivocados o que estas intentando hacer algo con un objeto que no lo permite es decir usar un dato como si fuera otro

//Posibles errores con su respectiva solucion//

En caso de tener un error y estar todo correcto cerrar el servidor con control + c y abrir una nueva terminal ya que la terminal almacena cache y puede ocacionar errores

Cuidado con la identacion -usa python indent o algo similar
Formatea el codigo -manual o con prettier o algo similar

Cuidado con la ortografia y error de plural,singular,mayuscula,minuscula o saltarse letras

Asegurate de que la direccion path este bien escrita y acorde en los diferentes archivos para evitar el error page no found 


