function markField(id, key, hint) {
    removeColor()
    if (hint.length > 1) {
        let hintElement = document.getElementById(id).parentElement
        let field = document.getElementById(hint[1])

        if (!hintElement.open && key == 2) {
            hint[1].forEach(element => {
                document.getElementById(element).style.backgroundColor = "rgba(255,0,0,0.37)"
            })
        } else if (hintElement.open && key == 2) {
            hint[1].forEach(element => {
                document.getElementById(element).style.backgroundColor = ""
            })
        }
        if (!hintElement.open && (key == 3 || key == 4)) {
            field.style.backgroundColor = "rgba(255,0,0,0.37)"
            if (key == 4) {
                field.placeholder = hint[2]
            }
        } else if (hintElement.open && (key == 3 || key == 4)) {
            field.style.backgroundColor = ""
            if (key == 4) {
                field.placeholder = ""
            }
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
    showCandidateButton()
    detailsClose()
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

    details.forEach((targetDetail) => {
        targetDetail.addEventListener("click", () => {
            details.forEach((detail) => {
                if (detail !== targetDetail) {
                    detail.removeAttribute("open")

                }
            })
        })
    })
}

function removeColor(){
    const fields = document.getElementsByClassName("sudoku-board-cell")
    for(let i = 0; i < fields.length; i++){
        let children = fields[i].children
        children[0].style.backgroundColor = ""
        children[0].placeholder = ""
    }
}
