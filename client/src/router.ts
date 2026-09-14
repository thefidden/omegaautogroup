import { createWebHistory, createRouter, type RouteLocationNormalized } from 'vue-router'
import MainView from "./pages/MainView.vue";
import CarListView from "./pages/CarListView.vue";
import CarView from "./pages/CarView.vue";
import { storeToRefs } from "pinia";
import { useStore } from "./stores/Store.ts";
import { useCarListFilterSet } from "./stores/CarListFilterSet.ts";
import { watch } from "vue";

export default createRouter({
    history: createWebHistory(),

    scrollBehavior(to, from, savedPosition) {
        if (savedPosition)
            return savedPosition

        if (to.hash)
            return { el: to.hash, behavior: 'smooth' }

        return { top: 0 }
    },

    routes: [
        {
            path: '/',
            component: MainView,
            name: 'main',
            beforeEnter: async(route: RouteLocationNormalized) => {
                document.title = 'Omega Auto Group'
            }
        },

        {
            path: '/cars/',
            component: CarListView,
            name: 'car-list',
            beforeEnter: async (route: RouteLocationNormalized) => {
                const carListFilterSet = useCarListFilterSet()
                const { brand } = storeToRefs(carListFilterSet)

                if (route.query.brand)
                    brand.value = route.query.brand as string

                document.title = `Автомобили ${ brand.value }`
            }
        },

        {
            path: '/cars/:id',
            component: CarView,
            name: 'car',
            props: (route: RouteLocationNormalized) => ( {
                id: route.params.id
            } ),
            beforeEnter: async (route: RouteLocationNormalized) => {
                const store = useStore()
                const { carID, car } = storeToRefs(store)
                carID.value = route.params.id as string

                watch(car, () => {
                    if (car)
                        document.title = `${car.value?.brand || ''} ${car.value?.model || ''}`.trim()
                })

            }
        }
    ]
})