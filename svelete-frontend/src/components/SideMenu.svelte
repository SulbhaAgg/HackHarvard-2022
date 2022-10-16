<script>
  import Icon from "svelte-icons-pack/Icon.svelte";
  import TiThMenu from "svelte-icons-pack/ti/TiThMenu";
  var menu;
  import { isActive, url } from '@roxi/routify'

  export let title="Harambe";
  const links = [
    ['/home', 'Home'],
    ['/history', 'History']
  ]
</script>

<ion-header collapse="fade" translucent="true">
  <ion-toolbar>
    <!--
    <ion-button slot="start" on:click={() => menu.toggle()}>
      <Icon src={TiThMenu} />
    </ion-button>-->
    <ion-title>{title}</ion-title>
  </ion-toolbar>
</ion-header>
<ion-menu
  side="start"
  menu-id="first"
  content-id="router-content"
  bind:this={menu}
>
  <ion-header>
    <ion-toolbar color="primary">
      <ion-title>Menu</ion-title>
    </ion-toolbar>
  </ion-header>
  <ion-content>
    <ion-list>
      {#each links as [path,name]}
        <ion-item>
          <a href={$url(path)}>
            {name}
          </a>
        </ion-item>
      {/each}
    </ion-list>
  </ion-content>
</ion-menu>
