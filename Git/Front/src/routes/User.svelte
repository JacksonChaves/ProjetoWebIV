<script>
    let resposta = "";
    async function sendForm(e){
        let formData = new FormData(e.target);
        let data = Object.fromEntries(formData.entries());
        const res = await fetch('http://localhost:8000/users/',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        const json = await res.json();
        resposta = JSON.stringify(json);
        resposta = JSON.stringify('Adicionado com sucesso');
    }
</script>
    
    <h2>New user</h2>
    
    <p>{resposta}</p>
    
    <form class="crud" on:submit|preventDefault={sendForm}>
        <input type="text" name="name" placeholder="User name" required autocomplete="off">
        <input type="text" name="email" placeholder="Email" required autocomplete="off">
        <input type="text" name="password" placeholder="password" required autocomplete="off">
        <input type="submit" value="add">
    </form>
    
    <style>
    form.crud{
        display: grid;
        grid-template-columns: 1fr;
        gap: 5px;
        row-gap: 10px;
    }
    .crud input[type=submit]{
        justify-self: baseline;
    }
    </style>
    