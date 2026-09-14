import { defineStore } from "pinia";

export const useCarListFilterSet = defineStore('car-list-filterset', {
    state: () => ({
        brand: ''
    })
})