<script setup lang="ts">

import { onMounted, watch } from "vue";
import { useStore } from "./stores/Store.ts";
import { useCarListFilterSet } from "./stores/CarListFilterSet.ts";
import { storeToRefs } from "pinia";
import Header from "./components/Header.vue";
import FooterMine from "./components/FooterMine.vue";

const store = useStore()
const { fetchAvailableBrands, fetchCars, fetchCar } = store
const { carID } = storeToRefs(store)

const carListFilterSet = useCarListFilterSet()
const { brand } = storeToRefs(carListFilterSet)

onMounted(async () => {
    await fetchAvailableBrands()
})

watch(brand, (newValue, oldValue) => {
    if (newValue !== oldValue)
        fetchCars({ brand: newValue })
})

watch(carID, (newValue, oldValue) => {
    if (newValue && newValue !== oldValue)
        fetchCar(newValue)
})

</script>

<template>
    <div class="app">
        <div class="ellipses" aria-hidden="true">
            <div class="ellipse" v-for="n in 7" :key="n"></div>
        </div>

        <div class="root">
            <router-view/>
            <FooterMine/>
        </div>

        <Header/>
    </div>

    <div class="noise"/>
</template>

<style scoped>
.app {
    position: relative;
    isolation: isolate;
    overflow: clip;
    min-height: 100dvh;
}

.root {
    position: relative;
    z-index: 1;

    display: flex;
    flex-direction: column;

    max-width: 1500px;
    min-height: 100dvh;
    margin: 0 auto;
}

.ellipses {
    --ellipse-small: max(420px, 36.458vw);
    --ellipse-large: max(600px, 52.083vw);

    position: absolute;
    inset: 0;
    z-index: 0;

    width: 100%;
    min-height: 3700px;
    height: auto;
    overflow: hidden;

    filter: blur(clamp(120px, 10.417vw, 200px));
    opacity: 0.6;
    transform: translateZ(0);
    pointer-events: none;
}

.ellipse {
    position: absolute;
    z-index: -3;

    background-color: var(--color-secondary);
    border-radius: 100%;
}

.ellipses .ellipse:nth-child(1) {
    left: 50%;
    transform: translateX(-50%) translateY(-50%);

    width: var(--ellipse-small);
    height: var(--ellipse-small);
}

.ellipses .ellipse:nth-child(2) {
    left: 0;
    top: 150px;
    transform: translateX(-50%);

    width: var(--ellipse-small);
    height: var(--ellipse-small);
}

.ellipses .ellipse:nth-child(3) {
    left: 100%;
    top: 150px;
    transform: translateX(-50%);

    width: var(--ellipse-small);
    height: var(--ellipse-small);
}

.ellipses .ellipse:nth-child(4) {
    left: 13.75vw;
    top: 709px;

    width: var(--ellipse-large);
    height: var(--ellipse-large);
}

.ellipses .ellipse:nth-child(5) {
    left: 100%;
    top: 1685px;
    transform: translateX(-50%);

    width: var(--ellipse-small);
    height: var(--ellipse-small);
}

.ellipses .ellipse:nth-child(6) {
    left: -10vw;
    top: 2064px;

    width: var(--ellipse-large);
    height: var(--ellipse-large);
}

.ellipses .ellipse:nth-child(7) {
    left: 50%;
    top: 100%;

    transform: translateX(-50%) translateY(-50%);

    width: var(--ellipse-large);
    height: var(--ellipse-large);
}

.noise {
    position: fixed;
    inset: 0;

    z-index: 9999;
    pointer-events: none;

    opacity: 0.8;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 180 180' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='.65'/%3E%3C/svg%3E");
    background-size: 180px 180px;
    mix-blend-mode: soft-light;
}

</style>
