import App from './App.svelte'
import { pwaStatusStream } from '$lib/pwa';  // do something with any stream in this lib here, to register the PWA
import { setupIonicSvelte } from '$ionic/svelte';
import type { PWAStatus } from '$Lib/pwa';

setupIonicSvelte();

pwaStatusStream.subscribe((status: PWAStatus) => {
  console.log("PWA status", status);

  if (status.updateFunction) {
    console.log("PWA updating itself in 4 secs......");
    setTimeout(() => {
      status.updateFunction();
    }, 4000);
  }
});
// if the page was prerendered, we want to remove the prerendered html
document.querySelector('[data-routify]')?.remove()
const app = new App({
  target: document.getElementById('app')
})

export default app


