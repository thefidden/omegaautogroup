import { defineStore } from "pinia";
import type { Car } from "../interfaces/Car.ts";
import type { CarListFilterSet } from "../interfaces/CarListFilterSet.ts";

export const useStore = defineStore('store', {
    state: () => ( {
        brands: [] as string[],
        cars: [] as Car[],
        car: null as Car | null,
        carID: '',

        loading: false,
        brandsLoading: false,
        carsLoading: false,
        carLoading: false
    } ),

    actions: {
        async fetchAvailableBrands() {
            this.brands = []
            this.brandsLoading = true

            try {
                const response = await fetch('/api/brands/?only_available=true')
                if (!response.ok) throw new Error(`brands request failed: ${response.status}`)
                const data: { name: string }[] = await response.json()
                this.brands = data.map(brand => brand.name)
            }
            catch (e) {
                console.log('fetch brands error', e)
                this.brands = []
            }
            finally {
                this.brandsLoading = false
            }
        },

        async fetchCars(filterSet: CarListFilterSet) {
            this.cars = []
            this.carsLoading = true

            const url = new URL('/api/client/cars/', window.location.origin)

            if (filterSet.brand) url.searchParams.append('brand', filterSet.brand)

            try {
                const response = await fetch(url)
                if (!response.ok) throw new Error(`cars request failed: ${response.status}`)
                this.cars = await response.json()
                console.log(this.cars)
            }
            catch (e) {
                console.log('fetch cars error', e)
                this.cars = []
            }
            finally {
                this.carsLoading = false
            }
        },

        async fetchCar(id: string) {
            this.car = null
            this.carLoading = true

            try {
                const response = await fetch(`/api/client/cars/${id}`)
                if (!response.ok) throw new Error(`car request failed: ${response.status}`)
                const data = await response.json() as Car
                if (!Array.isArray(data.images)) throw new Error('car response has no images')
                this.car = data
            }
            catch (e) {
                console.log('fetch car error', e)
                this.car = null
            }
            finally {
                this.carLoading = false
            }
        }
    }
})
