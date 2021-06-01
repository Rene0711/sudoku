function writeNumber() {
    const cells = document.getElementsByClassName("sudoku-board-cell")
    var map = {};
    for (let i = 0; i < cells.length; i++) {
        cells[i].addEventListener("keydown", function (e) {
            if (e.key == 1) cells[i].children[0].value = e.key
            if (e.key == 2) cells[i].children[0].value = e.key
            if (e.key == 3) cells[i].children[0].value = e.key
            if (e.key == 4) cells[i].children[0].value = e.key
            if (e.key == 5) cells[i].children[0].value = e.key
            if (e.key == 6) cells[i].children[0].value = e.key
            if (e.key == 7) cells[i].children[0].value = e.key
            if (e.key == 8) cells[i].children[0].value = e.key
            if (e.key == 9) cells[i].children[0].value = e.key

            if (e.keyCode == 8 || e.keyCode == 46) cells[i].children[0].value = ''
            if (e.keyCode == 65 && e.keyCode == 68) {
                cells[i].children[1].children[0].children[0].value = ""
                cells[i].children[1].children[0].children[1].innerHTML = "&nbsp;"
            }
        })
    }
}

function disableStarterNumbers() {
    const cells = document.getElementsByClassName("sudoku-board-cell")
    for (let i = 0; i < cells.length; i++) {
        if (cells[i].children[0].value) {
            cells[i].children[0].clickable = false
        }
    }
}


function markField(id, key, hint) {
    removeColor()
    if (hint.length > 1) {
        let algoName = document.getElementById("key-1-p")
        if (algoName.innerHTML.includes("Naked Single") || algoName.innerHTML.includes("Hidden Single")) {
            naked_hiddenSingle(id, key, hint)
        } else if (algoName.innerHTML.includes("Locked Candidates Type") || algoName.innerHTML.includes("Naked Pair")) {
            locked_candidates(id, key, hint)
        }

    }
}

function showCandidates(candidates) {
    if (document.getElementById("candidates_checkbox").checked) {
        let candidateFields = document.getElementsByClassName("candidate-box")
        for (let i = 0; i < candidateFields.length; i++) {
            candidateFields[i].removeAttribute("style")
        }
        const letters = "ABCDEFGHI"
        const numbers = "123456789"
        for (let i = 0; i < letters.length; i++) {
            let l = letters.charAt(i)
            for (let j = 0; j < numbers.length; j++) {
                let n = numbers.charAt(j)
                let field_candidates = document.getElementById("candidates-" + l + n).children
                candidates[l + n].forEach(element => {
                    field_candidates[element - 1].children[0].value = element
                    field_candidates[element - 1].children[1].innerHTML = element
                })
            }
        }
    } else {
        let candidateFields = document.getElementsByClassName("candidate-box")
        for (let i = 0; i < candidateFields.length; i++) {
            candidateFields[i].style.display = "none"
        }
    }
}

function onSiteLoad() {
    //disableStarterNumbers()
    showCandidateButton()
    detailsClose()
    writeNumber()
}

function showCandidateButton() {
    var hints = document.getElementById("key-1")
    var button = document.getElementById("candidateButton")
    if (hints == null) {
        button.hidden = true
    } else {
        button.hidden = false
    }
}

function detailsClose() {
    const details = document.querySelectorAll("details")

    details.forEach(targetDetail => {
        targetDetail.addEventListener("click", () => {
            details.forEach((detail) => {
                if (detail !== targetDetail) {
                    detail.removeAttribute("open")

                }
            })
        })
    })
}

function removeColor() {
    const fields = document.getElementsByClassName("sudoku-board-cell")
    for (let i = 0; i < fields.length; i++) {
        let children = fields[i].children
        children[0].style.backgroundColor = ""
        children[0].placeholder = ""
    }
}

function naked_hiddenSingle(id, key, hint) {
    let hintElement = document.getElementById(id).parentElement
    let field = document.getElementById(hint[1])
    let candidateField = document.getElementById(hint[1] + "-" + hint[2])

    // Hinweis 2
    if (!hintElement.open && key == 2) {
        hint[1].forEach(element => {
            document.getElementById(element).style.backgroundColor = "rgba(255,0,0,0.37)"
        })
    } else if (hintElement.open && key == 2) {
        hint[1].forEach(element => {
            document.getElementById(element).style.backgroundColor = ""
        })
    }

    // Hinweis 3
    if (!hintElement.open && (key == 3)) {
        field.style.backgroundColor = "rgba(255,0,0,0.37)"

    } else if (hintElement.open && (key == 3)) {
        field.style.backgroundColor = ""
    }

    // Hinweis 4
    if (!hintElement.open && (key == 4)) {
        if (document.getElementById("candidates_checkbox").checked) {
            candidateField.style.backgroundColor = "rgba(0,255,0,0.37)"
        } else {
            alert("Bitte aktivieren Sie alle Kandidaten zuerst")
        }
    } else if (hintElement.open && (key == 4)) {
        candidateField.style.backgroundColor = ""
    }
}

function locked_candidates(id, key, hint) {
    let hintElement = document.getElementById(id).parentElement

    // Hinweis 2
    if (!hintElement.open && key == 2) {
        hint[1].forEach(element => {
            document.getElementById(element).style.backgroundColor = "rgba(255,0,0,0.37)"
        })
    } else if (hintElement.open && key == 2) {
        hint[1].forEach(element => {
            document.getElementById(element).style.backgroundColor = ""
        })
    }

    // Hinweis 3
    if (!hintElement.open && key == 3) {
        hint[1].forEach(element => {
            document.getElementById(element).style.backgroundColor = "rgba(255,0,0,0.37)"
        })
    } else if (hintElement.open && key == 3) {
        hint[1].forEach(element => {
            document.getElementById(element).style.backgroundColor = ""
        })
    }

    // Hinweis 4
    if (!hintElement.open && (key == 4)) {
        if (document.getElementById("candidates_checkbox").checked) {
            hint[1].forEach(element => {
                document.getElementById(element + "-" + hint[2]).style.backgroundColor = "rgba(0,255,0,0.37)"
            })
            hint[3].forEach(element => {
                document.getElementById(element + "-" + hint[2]).style.backgroundColor = "rgba(255,0,0,0.37)"
            })
        } else {
            alert("Bitte aktivieren Sie alle Kandidaten zuerst")
        }
    } else if (hintElement.open && (key == 4)) {
        hint[1].forEach(element => {
            document.getElementById(element + "-" + hint[2]).style.backgroundColor = ""
        })
        hint[3].forEach(element => {
            document.getElementById(element + "-" + hint[2]).style.backgroundColor = ""
        })
    }


}
