document.addEventListener("DOMContentLoaded", function() {

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
        divContainer.appendChild(funcionInferior)
        divContainer.appendChild(funcionSuperior)

        functionContainer.appendChild(divContainer)
    })

    var funtionCreated = []

    document.getElementById('calcular').addEventListener("click", () => {
        let functionContainer = document.querySelector('.functionContainer')
        funtionCreated = []

        functionContainer.childNodes.forEach(element => {
            if (element.nodeType === 1){
                funtionCreated.push({
                    function : element.querySelector(".getFunction").value,
                    upper_limit : element.querySelector(".getUpValue").value,
                    lower_limit : element.querySelector(".getDownValue").value,
                })
            }
        })
        console.log(funtionCreated)

        const urlToTabulate = 'http://127.0.0.1:5000/api/utils/tabulate_function'
        let traces = []
        
        funtionCreated.forEach(functionToTabulate => {
            fetch(urlToTabulate, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(functionToTabulate)
            }).then(response => {
                if (!response){
                    throw new Error('HTTP error ' + response.status);
                }
                return response.json()
            }).then(data => {
                traces.push({
                    x:data.t_values,
                    y:data.y_values,
                    mode: 'lines+markers',
                    type: 'scatter'
                })
            }).then(()=>{
                Plotly.newPlot('plot1', traces);
            })
        })        
        
        const urlToCalculateFourier = 'http://127.0.0.1:5000/api/calculate-fourier'

        let period = document.querySelector(".getPeriod").value
        var trace1 = null 
        fetch(urlToCalculateFourier + '?period=' + period, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(funtionCreated)

        }).then(response => {
            if (!response){
                throw new Error('HTTP error ' + response.status);
            }
            return response.json();
        }).then(data => {
            console.log(data)
            trace1 = ({
                x:data.tabulate.t_values,
                y:data.tabulate.y_values,
                mode: 'lines+markers',
                type: 'scatter'
            })
            Plotly.newPlot('plot2', [trace1]);
            aN.textContent = data.aN;
            bN.textContent = data.bN
            a0.textContent = data.a0
            MathJax.typesetPromise([document.getElementById("aN")]);
            MathJax.typesetPromise([document.getElementById("bN")]);
            console.log(aN)
        })
    })
});