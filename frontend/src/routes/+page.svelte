<script>
	let menu = 1;
	import Movie from "./Movie.svelte"
	import Artista from "./Artista.svelte"
	import User from "./User.svelte"
	import Nav from "./Nav.svelte"
	import UserList from "./UserList.svelte"
	import Favoritos from "./Favoritos.svelte"
	import BuscaArtista from "./BuscaArtista.svelte"
    import ArtistaList from "./ArtistaList.svelte";
    import BuscaFilmes from "./BuscaFilmes.svelte";

</script>

<Nav bind:menu/>

<div class="card">
	{#if menu === 1}
		<Movie/>
	{:else if menu === 2}
		<Artista/>
	{:else if menu === 3}
		<User/>
	{:else if menu === 4}
		<UserList/>
	{:else if menu === 5}
		<Favoritos/>
	{:else if menu === 6}
		<BuscaArtista/>	
	{:else if menu === 7}
		<ArtistaList/>	
	{:else if menu === 8}
		<BuscaFilmes/>	
	{/if}
</div>