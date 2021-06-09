function strategieLoad(hints) {
    console.log(hints[4])
    const cells = document.getElementsByClassName("sudoku-board-cell")
    for (let i = 0; i < cells.length; i++) {
        cells[i].addEventListener("keydown", function (e) {
            if (e.key == 1) correctCheck(1, cells[i], hints)
            if (e.key == 2) correctCheck(2, cells[i], hints)
            if (e.key == 3) correctCheck(3, cells[i], hints)
            if (e.key == 4) correctCheck(4, cells[i], hints)
            if (e.key == 5) correctCheck(5, cells[i], hints)
            if (e.key == 6) correctCheck(6, cells[i], hints)
            if (e.key == 7) correctCheck(7, cells[i], hints)
            if (e.key == 8) correctCheck(8, cells[i], hints)
            if (e.key == 9) correctCheck(9, cells[i], hints)

            if (e.shiftKey && e.keyCode == 49) correctCheck(1, cells[i], hints)
            if (e.shiftKey && e.keyCode == 50) correctCheck(2, cells[i], hints)
            if (e.shiftKey && e.keyCode == 51) correctCheck(3, cells[i], hints)
            if (e.shiftKey && e.keyCode == 52) correctCheck(4, cells[i], hints)
            if (e.shiftKey && e.keyCode == 53) correctCheck(5, cells[i], hints)
            if (e.shiftKey && e.keyCode == 54) correctCheck(6, cells[i], hints)
            if (e.shiftKey && e.keyCode == 55) correctCheck(7, cells[i], hints)
            if (e.shiftKey && e.keyCode == 56) correctCheck(8, cells[i], hints)
            if (e.shiftKey && e.keyCode == 57) correctCheck(9, cells[i], hints)

        })
    }
}


function correctCheck(key, cell, hints) {
    let id = cell.children[0].id
    let correctInfo = document.getElementById("correctInfo")
    if (window.location.href.includes('single')) {
        if (id == hints[4][1] && key == parseInt(hints[4][2])) {
            correctInfo.innerText = "Super du hast den richtigen Wert gefunden."
        } else {
            correctInfo.innerText = "Das war leider der falsche Wert."
            cell.children[0].style.color = "rgb(255,0,0)"
        }
    } else if (window.location.href.includes('hidden_pair')) {
        let correctCheck = false
        hints[4][1].forEach(fieldID => {
            let field = document.getElementById(fieldID).parentElement
            for (let i = 0; i < 9; i++) {
                let childValue = field.children[1].children[i].children[0].value
                if (childValue != "" && !hints[4][2].includes(key) && hints[4][1].includes(id)) {
                    correctCheck = true
                }
            }
        })
        if (correctCheck) {
            correctInfo.innerText = "Super du hast einen richtigen Wert gefunden."
        } else {
            correctInfo.innerText = "Das war leider ein falscher Wert."
        }
    } else {
        if ("123456789".includes(hints[4][2])) {
            if (hints[4][3].includes(id) && hints[4][2] == key) {
                correctInfo.innerText = "Super du hast einen richtigen Wert gefunden."
            } else {
                correctInfo.innerText = "Das war leider ein falscher Wert."
            }
        } else {
            if (hints[4][3].includes(id) && hints[4][2].includes(key)) {
                correctInfo.innerText = "Super du hast einen richtigen Wert gefunden."
            } else {
                correctInfo.innerText = "Das war leider ein falscher Wert."
            }
        }
    }
}