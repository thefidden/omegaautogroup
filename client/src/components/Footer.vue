<script setup lang="ts">
import { computed } from "vue"
import { storeToRefs } from "pinia"
import { useRoute } from "vue-router"
import BlockGlass from "./BlockGlass.vue"
import ButtonShiftingTextWithIcon from "./ButtonShiftingTextWithIcon.vue"
import { useStore } from "../stores/Store.ts"
import { useCarListFilterSet } from "../stores/CarListFilterSet.ts"

const route = useRoute()
const { car } = storeToRefs(useStore())
const { brand } = storeToRefs(useCarListFilterSet())

const breadcrumbs = computed(() => {
    const home = { label: "Главная страница", href: "/" }
    if (route.name === "main") return [{ label: home.label }]

    const catalog = { label: "Все автомобили", href: "/#brand-selection" }
    const currentBrand = car.value?.brand || brand.value ||
        (typeof route.query.brand === "string" ? route.query.brand : "")

    if (route.name === "car-list") {
        return [home, catalog, {
            label: currentBrand ? `Автомобили ${currentBrand}` : "Автомобили"
        }]
    }

    if (route.name === "car") {
        const carPage = currentBrand
            ? `/cars/?brand=${encodeURIComponent(currentBrand)}`
            : undefined
        return [home, catalog, {
            label: currentBrand ? `Автомобили ${currentBrand}` : "Автомобили",
            href: carPage
        }, {
            label: car.value ? `${car.value.brand} ${car.value.model}` : "Автомобиль"
        }]
    }

    return [{ label: home.label }]
})
</script>

<template>
    <block-glass class="footer" style="background-color: var(--color-primary-30)">
        <nav aria-label="Навигация по страницам">
            <template v-for="(page, index) in breadcrumbs" :key="`${page.label}-${index}`">
                <ButtonShiftingTextWithIcon
                    v-if="page.href"
                    class="breadcrumb-link"
                    :href="page.href"
                    icon-alt=""
                >{{ page.label }}</ButtonShiftingTextWithIcon>
                <span v-else class="breadcrumb-current">{{ page.label }}</span>
            </template>
        </nav>
    </block-glass>
</template>

<style scoped>
.footer {
    position: fixed;
    z-index: 10;
    left: 30px;
    bottom: 30px;
    box-sizing: border-box;
    max-width: calc(100vw - 60px);
    min-height: 60px;
    padding: 10px 20px;
    user-select: none;
}

nav {
    display: flex;
    align-items: center;
    max-width: 100%;
    overflow-x: auto;
    scrollbar-width: none;
}

nav::-webkit-scrollbar { display: none; }

.breadcrumb-link,
.breadcrumb-current {
    flex: 0 0 auto;
    font-size: 16px;
    font-weight: 400;
    white-space: nowrap;
}

.footer :deep(.breadcrumb-link) {
    padding: 0 10px;
}

.breadcrumb-current {
    padding: 0 10px;
    color: rgba(255, 255, 255, .9);
}

@media (max-width: 600px) {
    .footer {
        left: 16px;
        bottom: 16px;
        max-width: calc(100vw - 32px);
    }
}
</style>
