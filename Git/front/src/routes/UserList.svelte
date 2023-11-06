<script> 

	  let resposta = "";
	  let promise = getUsers();
	  async function getUsers() {
	  // faz um request GET para endpoint /Users
		const res = await fetch(`http://localhost:8000/users`);
		const text = await res.json();
		if (res.ok) { return text; } 
	  	else { throw new Error(text);}
	  }
	  function handleClick() {
		promise = getUsers();
	  }
	  
	  async function deleteUser(e) {
		e.preventDefault();
		const userId = e.target.elements.id.value;
		const userName = e.target.elements.name.value;

		const res = await fetch(`http://localhost:8000/users/${userId}`, {
			method: 'DELETE',
			headers: {'Content-Type': 'application/json'}
		});

		if (res.ok) {
			resposta = `Usuário ${userName} excluído`;
			promise = getUsers();
		}
	  }

	

  </script>
  
  <button on:click={handleClick}> Carregar Usuários... </button>
  
  {#await promise}
	  <p>...loading</p>
  {:then users}
	<h1>Lista de Usuários</h1>
	{#each users as user}
        <p>ID: {user.id} - Nome: {user.name} - Email: {user.email}</p>
		
        <form on:submit|preventDefault={deleteUser}>
			<input type="hidden" name="name" value="{user.name}">
			<input type="hidden" name="id" value="{user.id}">
			<button type="submit">Excluir Usuário</button>
		</form>
		
	{/each}
  
  {:catch error}
	  <p style="color: red">{error.message}</p>
  {/await}