<script>
    export let menu;
  </script>
  
  <div id="componente-nav">
    <ul>
      <!-- svelte-ignore a11y-invalid-attribute -->
      <li><a href="/" class="menu-link" on:click|preventDefault={() => (menu = 1)}>Filmes</a></li>
      <li><a href="/" class="menu-link" on:click|preventDefault={() => (menu = 2)}>Artista</a></li>
      <li><a href="/" class="menu-link" on:click|preventDefault={() => (menu = 3)}>Users Add</a></li>
      <li><a href="/" class="menu-link" on:click|preventDefault={() => (menu = 4)}>User List</a></li> 
      <li><a href="/" class="menu-link" on:click|preventDefault={() => (menu = 5)}>Favoritos</a></li>   
      <li><a href="/" class="menu-link" on:click|preventDefault={() => (menu = 6)}>Busca Artistas</a></li>   
      <li><a href="/" class="menu-link" on:click|preventDefault={() => (menu = 7)}>Artistas Favoritados</a></li>
      <li><a href="/" class="menu-link" on:click|preventDefault={() => (menu = 8)}>Busca Filmes</a></li>   
   
    </ul>
  </div>
  
  <style>
    #componente-nav {
    background-color: #333; 
    padding: 10px;
    }

    ul {
    list-style: none; 
    padding: 0;
    }

    li {
    display: inline-block;
    margin-right: 20px; 
    }

    .menu-link {
    text-decoration: none; 
    color: #fff; 
    font-size: 18px; 
    transition: color 0.3s; 
    }

    .menu-link:hover {
    color: #ff9900; 
    }
  </style>