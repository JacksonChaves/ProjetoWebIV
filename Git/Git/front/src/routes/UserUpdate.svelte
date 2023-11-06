<script>
    let resposta = "";
    async function sendForm(e, method, url) {
        e.preventDefault();
        let formData = new FormData(e.target);
        let data = Object.fromEntries(formData.entries());

        const res = await fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        const json = await res.json();
        resposta = JSON.stringify(json);
    }

    async function updateUser(e) {
    const userId = e.target.querySelector('input[name="id"]').value;
    sendForm(e, 'PUT', `http://localhost:8000/users/${userId}`);
    }
</script>

<h2>Update user</h2>

<form class="crud" on:submit|preventDefault={updateUser}>
    <input type="text" name="name" placeholder="New name" autocomplete="off">
    <input type="text" name="email" placeholder="New email" autocomplete="off">
    <input type="text" name="password" placeholder="New password" autocomplete="off">
    <!-- svelte-ignore missing-declaration -->
    <input type="hidden" name="id" value="{user.id}">
    <input type="submit" value="Update">
</form>
