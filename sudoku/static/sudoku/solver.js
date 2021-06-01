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

            if (e.shiftKey && e.keyCode == 49) setCandidate(cells[i].children[1].children[0], 1)
            if (e.shiftKey && e.keyCode == 50) setCandidate(cells[i].children[1].children[1], 2)
            if (e.shiftKey && e.keyCode == 51) setCandidate(cells[i].children[1].children[2], 3)
            if (e.shiftKey && e.keyCode == 52) setCandidate(cells[i].children[1].children[3], 4)
            if (e.shiftKey && e.keyCode == 53) setCandidate(cells[i].children[1].children[4], 5)
            if (e.shiftKey && e.keyCode == 54) setCandidate(cells[i].children[1].children[5], 6)
            if (e.shiftKey && e.keyCode == 55) setCandidate(cells[i].children[1].children[6], 7)
            if (e.shiftKey && e.keyCode == 56) setCandidate(cells[i].children[1].children[7], 8)
            if (e.shiftKey && e.keyCode == 57) setCandidate(cells[i].children[1].children[8], 9)

            if (e.keyCode == 37) arrowMoves(e.keyCode)
            if (e.keyCode == 38) arrowMoves(e.keyCode)
            if (e.keyCode == 39) arrowMoves(e.keyCode)
            if (e.keyCode == 40) arrowMoves(e.keyCode)
        })
    }
}

function arrowMoves(key) {
    let focusedElement = document.activeElement
    const letters = "ABCDEFGHI"

    if (key == 37) {
        let id = focusedElement.id
        if (id.charAt(0) != "A") {
            let newID = letters.charAt(letters.indexOf(id.charAt(0)) - 1) + id.charAt(1)
            document.getElementById(newID).focus()
        }
    } else if (key == 39) {
        let id = focusedElement.id
        if (id.charAt(0) != "I") {
            let newID = letters.charAt(letters.indexOf(id.charAt(0)) + 1) + id.charAt(1)
            document.getElementById(newID).focus()
        }
    } else if (key == 38) {
        let id = focusedElement.id
        if (id.charAt(1) != "1") {
            let newID = id.charAt(0) + (parseInt(id.charAt(1)) - 1)
            document.getElementById(newID).focus()
        }
    } else {
        let id = focusedElement.id
        if (id.charAt(1) != "9") {
            let newID = id.charAt(0) + (parseInt(id.charAt(1)) + 1)
            document.getElementById(newID).focus()
        }
    }
}

function setCandidate(field, key) {
    if (field.children[0].value == "") {
        field.children[0].value = key
        field.children[1].innerHTML = key
    } else {
        field.children[0].value = ""
        field.children[1].innerHTML = "&nbsp;"

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
        } else if (algoName.innerHTML.includes("Locked Candidates Type")) {
            locked_candidates(id, key, hint)
        } else if (algoName.innerHTML.includes("Hidden Pair")) {
            hidden_subsets(id, key, hint)
        } else if (algoName.innerHTML.includes("Naked")) {
            naked_subsets(id, key, hint)
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

function naked_subsets(id, key, hint) {
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
                for (let i of hint[2]) {
                    if (document.getElementById(element + "-" + i).children[0].value != '') {
                        document.getElementById(element + "-" + i).style.backgroundColor = "rgba(0,255,0,0.37)"
                    }
                }

            })
            hint[3].forEach(element => {
                for (let i of hint[2]) {
                    if (document.getElementById(element + "-" + i).children[0].value != '') {
                        document.getElementById(element + "-" + i).style.backgroundColor = "rgba(255,0,0,0.37)"
                    }
                }

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


function hidden_subsets(id, key, hint) {
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
                document.getElementById(element + "-" + hint[2][0]).style.backgroundColor = "rgba(0,255,0,0.37)"
                document.getElementById(element + "-" + hint[2][1]).style.backgroundColor = "rgba(0,255,0,0.37)"

                for (let i = 1; i <= 9; i++) {
                    if (document.getElementById(element + "-" + i).children[0].value != ''
                        && document.getElementById(element + "-" + i).children[0].value != hint[2][0]
                        && document.getElementById(element + "-" + i).children[0].value != hint[2][1]) {
                        document.getElementById(element + "-" + i).style.backgroundColor = "rgba(255,0,0,0.37)"
                    }
                }
            })
        } else {
            alert("Bitte aktivieren Sie alle Kandidaten zuerst")
        }
    } else if (hintElement.open && (key == 4)) {
        hint[1].forEach(element => {
            document.getElementById(element + "-" + hint[2][0]).style.backgroundColor = ""
            document.getElementById(element + "-" + hint[2][1]).style.backgroundColor = ""

            for (let i = 1; i <= 9; i++) {
                if (document.getElementById(element + "-" + i).children[0].value != ''
                    && document.getElementById(element + "-" + i).children[0].value != hint[2][0]
                    && document.getElementById(element + "-" + i).children[0].value != hint[2][1]) {
                    document.getElementById(element + "-" + i).style.backgroundColor = ""
                }
            }


        })
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
