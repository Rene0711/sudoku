function keyHandler() {
    const cells = document.getElementsByClassName("sudoku-board-cell")
    for (let i = 0; i < cells.length; i++) {
        cells[i].addEventListener("keydown", function (e) {
            if (e.key == 1) cells[i].children[0].value = e.key , toggleCandidates(cells[i], false), inCheck(e.key, cells[i], 0)
            if (e.key == 2) cells[i].children[0].value = e.key , toggleCandidates(cells[i], false), inCheck(e.key, cells[i], 0)
            if (e.key == 3) cells[i].children[0].value = e.key , toggleCandidates(cells[i], false), inCheck(e.key, cells[i], 0)
            if (e.key == 4) cells[i].children[0].value = e.key , toggleCandidates(cells[i], false), inCheck(e.key, cells[i], 0)
            if (e.key == 5) cells[i].children[0].value = e.key , toggleCandidates(cells[i], false), inCheck(e.key, cells[i], 0)
            if (e.key == 6) cells[i].children[0].value = e.key , toggleCandidates(cells[i], false), inCheck(e.key, cells[i], 0)
            if (e.key == 7) cells[i].children[0].value = e.key , toggleCandidates(cells[i], false), inCheck(e.key, cells[i], 0)
            if (e.key == 8) cells[i].children[0].value = e.key , toggleCandidates(cells[i], false), inCheck(e.key, cells[i], 0)
            if (e.key == 9) cells[i].children[0].value = e.key , toggleCandidates(cells[i], false), inCheck(e.key, cells[i], 0)

            if (e.keyCode == 8 || e.keyCode == 46) cells[i].children[0].value = '' , toggleCandidates(cells[i], true)

            if (e.shiftKey && e.keyCode == 49) setCandidate(cells[i].children[1].children[0], 1), inCheck(1, cells[i], 1)
            if (e.shiftKey && e.keyCode == 50) setCandidate(cells[i].children[1].children[1], 2), inCheck(2, cells[i], 1)
            if (e.shiftKey && e.keyCode == 51) setCandidate(cells[i].children[1].children[2], 3), inCheck(3, cells[i], 1)
            if (e.shiftKey && e.keyCode == 52) setCandidate(cells[i].children[1].children[3], 4), inCheck(4, cells[i], 1)
            if (e.shiftKey && e.keyCode == 53) setCandidate(cells[i].children[1].children[4], 5), inCheck(5, cells[i], 1)
            if (e.shiftKey && e.keyCode == 54) setCandidate(cells[i].children[1].children[5], 6), inCheck(6, cells[i], 1)
            if (e.shiftKey && e.keyCode == 55) setCandidate(cells[i].children[1].children[6], 7), inCheck(7, cells[i], 1)
            if (e.shiftKey && e.keyCode == 56) setCandidate(cells[i].children[1].children[7], 8), inCheck(8, cells[i], 1)
            if (e.shiftKey && e.keyCode == 57) setCandidate(cells[i].children[1].children[8], 9), inCheck(9, cells[i], 1)

            if (e.keyCode == 37) arrowMoves(e.keyCode)
            if (e.keyCode == 38) arrowMoves(e.keyCode)
            if (e.keyCode == 39) arrowMoves(e.keyCode)
            if (e.keyCode == 40) arrowMoves(e.keyCode)

        })
    }
}

function inCheck(key, cell, type) {
    let id = cell.children[0].id
    let number = id.charAt(1)
    let letter = id.charAt(0)
    const letters = "ABCDEFGHI"
    const numbers = "123456789"
    let buddies = []

    for (let i = 0; i < letters.length; i++) {
        let l = letters.charAt(i)
        if (id != l + number) {
            buddies.push(document.getElementById(l + number))
        }
    }
    for (let i = 0; i < numbers.length; i++) {
        let n = numbers.charAt(i)
        if (id != letter + n) {
            buddies.push(document.getElementById(letter + n))
        }
    }
    squares_switch(id).forEach(field => {
        if (id != field) {
            buddies.push(document.getElementById(field))
        }
    })
    let check = false
    buddies.forEach(buddie => {
        if (buddie.value == key) {
            if (type == 0) {
                cell.children[0].style.color = "rgb(255,0,0)"
                check = true
            } else {
                cell.children[1].children[key - 1].style.color = "rgb(255,0,0)"
                check = true
            }
        } else if(!check) {
            if (type == 0) {
                cell.children[0].style.color = "rgb(0,0,0)"
            } else {
                cell.children[1].children[key - 1].style.color = "rgb(0,0,0)"
            }
        }
    })
}


function superFancy() {
    const candidateFields = document.getElementsByClassName("candidate_box")
    const algoName = document.getElementById("key-1-p")
    document.addEventListener("keydown", function (e) {
        if (e.code === "KeyA") {
            if (algoName.innerHTML.includes("Naked Single") || algoName.innerHTML.includes("Hidden Single")) {
                for (let i = 0; i < candidateFields.length; i++) {
                    if (candidateFields[i].style.backgroundColor === "rgba(0, 255, 0, 0.37)") {
                        let singleNumber = candidateFields[i].children[0].value
                        let parentCell = candidateFields[i].parentElement.parentElement

                        for (let i = 0; i < 9; i++) {
                            parentCell.children[1].children[i].children[0].value = ""
                            parentCell.children[1].children[i].children[1].innerHTML = "&nbsp;"
                        }

                        parentCell.children[0].value = singleNumber
                    }
                }
                removeColors()
            } else {
                for (let i = 0; i < candidateFields.length; i++) {
                    if (candidateFields[i].style.backgroundColor === "rgba(255, 0, 0, 0.37)") {
                        candidateFields[i].children[0].value = ""
                        candidateFields[i].children[1].innerHTML = "&nbsp;"

                    }
                }
                removeColors()
            }


        }
    })
}

function toggleCandidates(cell, toggle) {
    if (!toggle) {
        for (let i = 0; i < 9; i++) {
            cell.children[1].children[i].style.display = "none"
        }
    } else {
        for (let i = 0; i < 9; i++) {
            cell.children[1].children[i].style.display = ""

        }
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

let infoCount = 0

function markField(id, key, hint) {
    let algoName = document.getElementById("key-1-p")
    console.log(algoName.innerHTML)
    if (algoName.innerHTML.includes("Naked Single") || algoName.innerHTML.includes("Hidden Single")) {
        naked_hiddenSingle(id, key, hint)
    } else if (algoName.innerHTML.includes("Locked Candidates Type")) {
        locked_candidates(id, key, hint)
    } else if (algoName.innerHTML.includes("Hidden Pair")) {
        hidden_subsets(id, key, hint)
    } else if (algoName.innerHTML.includes("Naked")) {
        naked_subsets(id, key, hint)
    } else {
        locked_candidates(id, key, hint)
    }
    if (infoCount == 0 && window.location.href.includes('sudoku-solver')) {
        algoName.innerHTML = algoName.innerHTML + ' <a style="color: #f53978" target="_blank" rel="noopener noreferrer" href="/strategies?name=' + hint [1] + '">Mehr Infos</a>'
        infoCount++
    }
}

function showCandidates(candidates) {
    let candidateFields = document.getElementsByClassName("candidate_box")
    if (document.getElementById("candidates_checkbox").checked) {
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
        for (let i = 0; i < candidateFields.length; i++) {
            candidateFields[i].style.display = "none"
        }
    }
}

function onSiteLoad() {
    superFancy()
    //disableStarterNumbers()
    detailsClose()
    keyHandler()
    showCandidateButton()
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

function removeColors() {
    const fields = document.getElementsByClassName("sudoku-board-cell")
    const candidateFields = document.getElementsByClassName("candidate_box")
    for (let i = 0; i < fields.length; i++) {
        let children = fields[i].children
        children[0].style.backgroundColor = ""
    }
    for (let i = 0; i < candidateFields.length; i++) {
        candidateFields[i].style.backgroundColor = ""
    }
}

function naked_subsets(id, key, hint) {
    let hintElement = document.getElementById(id).parentElement

    // Hinweis 2
    if (!hintElement.open && key == 2) {
        removeColors()
        hint[1].forEach(element => {
            document.getElementById(element).style.backgroundColor = "rgba(255,0,0,0.37)"
        })
    } else if (hintElement.open && key == 2) {
        removeColors()
    }

    // Hinweis 3
    if (!hintElement.open && key == 3) {
        removeColors()
        hint[1].forEach(element => {
            document.getElementById(element).style.backgroundColor = "rgba(255,0,0,0.37)"
        })
    } else if (hintElement.open && key == 3) {
        removeColors()
    }

    // Hinweis 4
    if (!hintElement.open && (key == 4)) {
        removeColors()
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
        removeColors()
    }
}


function hidden_subsets(id, key, hint) {
    let hintElement = document.getElementById(id).parentElement


    // Hinweis 2
    if (!hintElement.open && key == 2) {
        removeColors()
        hint[1].forEach(element => {
            document.getElementById(element).style.backgroundColor = "rgba(255,0,0,0.37)"
        })
    } else if (hintElement.open && key == 2) {
        removeColors()
    }

    // Hinweis 3
    if (!hintElement.open && key == 3) {
        removeColors()
        hint[1].forEach(element => {
            document.getElementById(element).style.backgroundColor = "rgba(255,0,0,0.37)"
        })
    } else if (hintElement.open && key == 3) {
        removeColors()
    }

    // Hinweis 4
    if (!hintElement.open && (key == 4)) {
        removeColors()
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
        removeColors()
    }

}

function naked_hiddenSingle(id, key, hint) {
    let hintElement = document.getElementById(id).parentElement
    let field = document.getElementById(hint[1])
    let candidateField = document.getElementById(hint[1] + "-" + hint[2])

    // Hinweis 2
    if (!hintElement.open && key == 2) {
        removeColors()
        hint[1].forEach(element => {
            document.getElementById(element).style.backgroundColor = "rgba(255,0,0,0.37)"
        })
    } else if (hintElement.open && key == 2) {
        removeColors()
    }

    // Hinweis 3
    if (!hintElement.open && (key == 3)) {
        removeColors()
        field.style.backgroundColor = "rgba(255,0,0,0.37)"

    } else if (hintElement.open && (key == 3)) {
        removeColors()
    }

    // Hinweis 4
    if (!hintElement.open && (key == 4)) {
        removeColors()
        if (document.getElementById("candidates_checkbox").checked) {
            candidateField.style.backgroundColor = "rgba(0,255,0,0.37)"
        } else {
            alert("Bitte aktivieren Sie alle Kandidaten zuerst")
        }
    } else if (hintElement.open && (key == 4)) {
        removeColors()
    }
}

function locked_candidates(id, key, hint) {
    let hintElement = document.getElementById(id).parentElement

    // Hinweis 2
    if (!hintElement.open && key == 2) {
        removeColors()
        hint[1].forEach(element => {
            document.getElementById(element).style.backgroundColor = "rgba(255,0,0,0.37)"
        })
    } else if (hintElement.open && key == 2) {
        removeColors()
    }

    // Hinweis 3
    if (!hintElement.open && key == 3) {
        removeColors()
        hint[1].forEach(element => {
            document.getElementById(element).style.backgroundColor = "rgba(255,0,0,0.37)"
        })
    } else if (hintElement.open && key == 3) {
        removeColors()
    }

    // Hinweis 4
    if (!hintElement.open && (key == 4)) {
        removeColors()
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
        removeColors()
    }


}

function squares_switch(key) {
    let fields
    switch (key) {
        case "A1":
            fields = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
            break;
        case "A2":
            fields = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
            break;
        case "A3":
            fields = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
            break;
        case "B1":
            fields = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
            break;
        case "B2":
            fields = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
            break;
        case "B3":
            fields = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
            break;
        case "C1":
            fields = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
            break;
        case "C2":
            fields = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
            break;
        case "C3":
            fields = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
            break;
        case "D1":
            fields = ["D1", "D2", "D3", "E1", "E2", "E3", "F1", "F2", "F3"]
            break;
        case "D2":
            fields = ["D1", "D2", "D3", "E1", "E2", "E3", "F1", "F2", "F3"]
            break;
        case "D3":
            fields = ["D1", "D2", "D3", "E1", "E2", "E3", "F1", "F2", "F3"]
            break;
        case "E1":
            fields = ["D1", "D2", "D3", "E1", "E2", "E3", "F1", "F2", "F3"]
            break;
        case "E2":
            fields = ["D1", "D2", "D3", "E1", "E2", "E3", "F1", "F2", "F3"]
            break;
        case "E3":
            fields = ["D1", "D2", "D3", "E1", "E2", "E3", "F1", "F2", "F3"]
            break;
        case "F1":
            fields = ["D1", "D2", "D3", "E1", "E2", "E3", "F1", "F2", "F3"]
            break;
        case "F2":
            fields = ["D1", "D2", "D3", "E1", "E2", "E3", "F1", "F2", "F3"]
            break;
        case "F3":
            fields = ["D1", "D2", "D3", "E1", "E2", "E3", "F1", "F2", "F3"]
            break;
        case "G1":
            fields = ["G1", "G2", "G3", "H1", "H2", "H3", "I1", "I2", "I3"]
            break;
        case "G2":
            fields = ["G1", "G2", "G3", "H1", "H2", "H3", "I1", "I2", "I3"]
            break;
        case "G3":
            fields = ["G1", "G2", "G3", "H1", "H2", "H3", "I1", "I2", "I3"]
            break;
        case "H1":
            fields = ["G1", "G2", "G3", "H1", "H2", "H3", "I1", "I2", "I3"]
            break;
        case "H2":
            fields = ["G1", "G2", "G3", "H1", "H2", "H3", "I1", "I2", "I3"]
            break;
        case "H3":
            fields = ["G1", "G2", "G3", "H1", "H2", "H3", "I1", "I2", "I3"]
            break;
        case "I1":
            fields = ["G1", "G2", "G3", "H1", "H2", "H3", "I1", "I2", "I3"]
            break;
        case "I2":
            fields = ["G1", "G2", "G3", "H1", "H2", "H3", "I1", "I2", "I3"]
            break;
        case "I3":
            fields = ["G1", "G2", "G3", "H1", "H2", "H3", "I1", "I2", "I3"]
            break;
        case "A4":
            fields = ["A4", "A5", "A6", "B4", "B5", "B6", "C4", "C5", "C6"]
            break;
        case "A5":
            fields = ["A4", "A5", "A6", "B4", "B5", "B6", "C4", "C5", "C6"]
            break;
        case "A6":
            fields = ["A4", "A5", "A6", "B4", "B5", "B6", "C4", "C5", "C6"]
            break;
        case "B4":
            fields = ["A4", "A5", "A6", "B4", "B5", "B6", "C4", "C5", "C6"]
            break;
        case "B5":
            fields = ["A4", "A5", "A6", "B4", "B5", "B6", "C4", "C5", "C6"]
            break;
        case "B6":
            fields = ["A4", "A5", "A6", "B4", "B5", "B6", "C4", "C5", "C6"]
            break;
        case "C4":
            fields = ["A4", "A5", "A6", "B4", "B5", "B6", "C4", "C5", "C6"]
            break;
        case "C5":
            fields = ["A4", "A5", "A6", "B4", "B5", "B6", "C4", "C5", "C6"]
            break;
        case "C6":
            fields = ["A4", "A5", "A6", "B4", "B5", "B6", "C4", "C5", "C6"]
            break;
        case "D4":
            fields = ["D4", "D5", "D6", "E4", "E5", "E6", "F4", "F5", "F6"]
            break;
        case "D5":
            fields = ["D4", "D5", "D6", "E4", "E5", "E6", "F4", "F5", "F6"]
            break;
        case "D6":
            fields = ["D4", "D5", "D6", "E4", "E5", "E6", "F4", "F5", "F6"]
            break;
        case "E4":
            fields = ["D4", "D5", "D6", "E4", "E5", "E6", "F4", "F5", "F6"]
            break;
        case "E5":
            fields = ["D4", "D5", "D6", "E4", "E5", "E6", "F4", "F5", "F6"]
            break;
        case "E6":
            fields = ["D4", "D5", "D6", "E4", "E5", "E6", "F4", "F5", "F6"]
            break;
        case "F4":
            fields = ["D4", "D5", "D6", "E4", "E5", "E6", "F4", "F5", "F6"]
            break;
        case "F5":
            fields = ["D4", "D5", "D6", "E4", "E5", "E6", "F4", "F5", "F6"]
            break;
        case "F6":
            fields = ["D4", "D5", "D6", "E4", "E5", "E6", "F4", "F5", "F6"]
            break;
        case "G4":
            fields = ["G4", "G5", "G6", "H4", "H5", "H6", "I4", "I5", "I6"]
            break;
        case "G5":
            fields = ["G4", "G5", "G6", "H4", "H5", "H6", "I4", "I5", "I6"]
            break;
        case "G6":
            fields = ["G4", "G5", "G6", "H4", "H5", "H6", "I4", "I5", "I6"]
            break;
        case "H4":
            fields = ["G4", "G5", "G6", "H4", "H5", "H6", "I4", "I5", "I6"]
            break;
        case "H5":
            fields = ["G4", "G5", "G6", "H4", "H5", "H6", "I4", "I5", "I6"]
            break;
        case "H6":
            fields = ["G4", "G5", "G6", "H4", "H5", "H6", "I4", "I5", "I6"]
            break;
        case "I4":
            fields = ["G4", "G5", "G6", "H4", "H5", "H6", "I4", "I5", "I6"]
            break;
        case "I5":
            fields = ["G4", "G5", "G6", "H4", "H5", "H6", "I4", "I5", "I6"]
            break;
        case "I6":
            fields = ["G4", "G5", "G6", "H4", "H5", "H6", "I4", "I5", "I6"]
            break;
        case "A7":
            fields = ["A7", "A8", "A9", "B7", "B8", "B9", "C7", "C8", "C9"]
            break;
        case "A8":
            fields = ["A7", "A8", "A9", "B7", "B8", "B9", "C7", "C8", "C9"]
            break;
        case "A9":
            fields = ["A7", "A8", "A9", "B7", "B8", "B9", "C7", "C8", "C9"]
            break;
        case "B7":
            fields = ["A7", "A8", "A9", "B7", "B8", "B9", "C7", "C8", "C9"]
            break;
        case "B8":
            fields = ["A7", "A8", "A9", "B7", "B8", "B9", "C7", "C8", "C9"]
            break;
        case "B9":
            fields = ["A7", "A8", "A9", "B7", "B8", "B9", "C7", "C8", "C9"]
            break;
        case "C7":
            fields = ["A7", "A8", "A9", "B7", "B8", "B9", "C7", "C8", "C9"]
            break;
        case "C8":
            fields = ["A7", "A8", "A9", "B7", "B8", "B9", "C7", "C8", "C9"]
            break;
        case "C9":
            fields = ["A7", "A8", "A9", "B7", "B8", "B9", "C7", "C8", "C9"]
            break;
        case "D7":
            fields = ["D7", "D8", "D9", "E7", "E8", "E9", "F7", "F8", "F9"]
            break;
        case "D8":
            fields = ["D7", "D8", "D9", "E7", "E8", "E9", "F7", "F8", "F9"]
            break;
        case "D9":
            fields = ["D7", "D8", "D9", "E7", "E8", "E9", "F7", "F8", "F9"]
            break;
        case "E7":
            fields = ["D7", "D8", "D9", "E7", "E8", "E9", "F7", "F8", "F9"]
            break;
        case "E8":
            fields = ["D7", "D8", "D9", "E7", "E8", "E9", "F7", "F8", "F9"]
            break;
        case "E9":
            fields = ["D7", "D8", "D9", "E7", "E8", "E9", "F7", "F8", "F9"]
            break;
        case "F7":
            fields = ["D7", "D8", "D9", "E7", "E8", "E9", "F7", "F8", "F9"]
            break;
        case "F8":
            fields = ["D7", "D8", "D9", "E7", "E8", "E9", "F7", "F8", "F9"]
            break;
        case "F9":
            fields = ["D7", "D8", "D9", "E7", "E8", "E9", "F7", "F8", "F9"]
            break;
        case "G7":
            fields = ["G7", "G8", "G9", "H7", "H8", "H9", "I7", "I8", "I9"]
            break;
        case "G8":
            fields = ["G7", "G8", "G9", "H7", "H8", "H9", "I7", "I8", "I9"]
            break;
        case "G9":
            fields = ["G7", "G8", "G9", "H7", "H8", "H9", "I7", "I8", "I9"]
            break;
        case "H7":
            fields = ["G7", "G8", "G9", "H7", "H8", "H9", "I7", "I8", "I9"]
            break;
        case "H8":
            fields = ["G7", "G8", "G9", "H7", "H8", "H9", "I7", "I8", "I9"]
            break;
        case "H9":
            fields = ["G7", "G8", "G9", "H7", "H8", "H9", "I7", "I8", "I9"]
            break;
        case "I7":
            fields = ["G7", "G8", "G9", "H7", "H8", "H9", "I7", "I8", "I9"]
            break;
        case "I8":
            fields = ["G7", "G8", "G9", "H7", "H8", "H9", "I7", "I8", "I9"]
            break;
        case "I9":
            fields = ["G7", "G8", "G9", "H7", "H8", "H9", "I7", "I8", "I9"]
            break;
    }
    return fields
}
