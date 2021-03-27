document.addEventListener("keyup", async function () {
    let keywordLength = document.querySelector(".keyword").value.length
    if (keywordLength >= 3) {
        const form = document.querySelector("form")
        const result = await fetch(form.action, {
            method: form.method,
            body: new URLSearchParams([...(new FormData(form))]),
        })
            .then((response) => response.json())
            .then((json) => json)
            .catch((error) => console.log(error))

        console.log(result)
        document.querySelector(".results").innerHTML = result
    }
})