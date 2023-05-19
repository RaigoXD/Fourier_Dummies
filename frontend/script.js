document.addEventListener("DOMContentLoaded", function() {
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");
    const width = canvas.width;
    const height = canvas.height;
    console.log("width: " + width + " height: " + height);
  
    // Función para dibujar el plano cartesiano
    function drawCartesianPlane() {
      // Dibujar el eje x
      ctx.beginPath();
      ctx.moveTo(0, height / 2);
      ctx.lineTo(width, height / 2);
      ctx.stroke();
  
      // Dibujar el eje y
      ctx.beginPath();
      ctx.moveTo(width / 2, 0);
      ctx.lineTo(width / 2, height);
      ctx.stroke();
    }
  
    // Función para dibujar un punto en el plano cartesiano
    function drawPoint(x, y, color) {
        ctx.fillStyle = color;
        ctx.fillRect(x + width / 2, -y + height / 2, 4, 4);
    }
  
    // Ejemplo de uso: dibujar un punto en las coordenadas (50, 100) de color rojo
    drawCartesianPlane();
    drawPoint(4, 100, "red");

    document.getElementById('agregar').addEventListener("click", () => {
        let functionContainer = document.querySelector('.functionContainer')
        let countDiv = 0
        
        functionContainer.childNodes.forEach(element => {
            if (element.nodeType === 1){
                countDiv += 1;
            }
        })

        countDiv += 1

        let divContainer = document.createElement('div');
        divContainer.classList.add('function', 'data' + countDiv);
        
        let funcionInput = document.createElement('input');
        funcionInput.classList.add('getFunction');
        funcionInput.setAttribute('type', 'text');
        
        let funcionSuperior = document.createElement('input');
        funcionSuperior.classList.add('getUpValue');
        funcionSuperior.setAttribute('type', 'text');
        
        let funcionInferior = document.createElement('input');
        funcionInferior.classList.add('getDownValue');
        funcionInferior.setAttribute('type', 'text');

        divContainer.appendChild(funcionInput)
        divContainer.appendChild(funcionSuperior)
        divContainer.appendChild(funcionInferior)

        functionContainer.appendChild(divContainer)
    })

    var funtionCreated = []

    document.getElementById('calcular').addEventListener("click", () => {
        let functionContainer = document.querySelector('.functionContainer')
        funtionCreated = []

        functionContainer.childNodes.forEach(element => {
            if (element.nodeType === 1){
                funtionCreated.push({
                    funcion : element.querySelector(".getFunction").value,
                    limite_superior : element.querySelector(".getUpValue").value,
                    limite_inferior : element.querySelector(".getDownValue").value,
                })
            }
        })
        console.log(funtionCreated)
    })
});
