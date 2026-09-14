<script setup lang="ts">
import EarthIcon from "../../assets/earth.svg"
import SearchIcon from "../../assets/search.svg"
import ShieldIcon from "../../assets/shield.svg"
import DeliveryIcon from "../../assets/delivery.svg"
import CarHighAngleView from "../../assets/car-high-angle-view.png"
import BlockGlass from "../BlockGlass.vue"
</script>

<template>
    <div class="sector3">
        <img class="carHighAngleView" :src="CarHighAngleView" alt="" aria-hidden="true" v-for="index in 2" :key="index"/>

        <block-glass class="cell heading" style="--background-color: var(--color-secondary-20);">
            Наши преимущества
        </block-glass>

        <block-glass class="cell brands">
            <img :src="EarthIcon" alt="Earth"/>
            <div class="name">Автомобили любых производителей</div>
            <div class="description">
                <span>Подберём автомобиль любой марки: китайской,</span>
                <span>европейской, японской, корейской или другой</span>
            </div>
        </block-glass>

        <block-glass class="cell review">
            <img :src="ShieldIcon" alt="Earth"/>
            <div class="name">Юридическая и техническая проверка</div>
            <div class="description">
                <span>Проверим историю, документы</span>
                <span>и техническое состояние автомобиля</span>
            </div>
        </block-glass>

        <block-glass class="cell search">
            <img :src="SearchIcon" alt="Earth"/>
            <div class="name">Тщательный подбор под запросы</div>
            <div class="description">
                <span>Подберём автомобиль нужной марки,</span>
                <span>модели и комплектации</span>
            </div>
        </block-glass>

        <block-glass class="cell escort">
            <img :src="DeliveryIcon" alt="Earth"/>
            <div class="name">Сопровождение до получения</div>
            <div class="description">
                <span>Организуем процесс покупки, доставки</span>
                <span>и передачи автомобиля вам</span>
            </div>
        </block-glass>
    </div>
</template>

<style scoped>
.sector3 {
    position: relative;

    width: 100%;
    height: 800px;

    display: grid;
    grid-template-areas:
            ". header header ."
            "brands brands search search"
            "review review escort escort";
    grid-template-columns: 1fr 1fr 1fr 1fr;
    grid-template-rows: 0.5fr 1fr 1fr;
    grid-gap: 100px;

    justify-items: center;
    align-items: center;
}

.cell {
    width: 100%;
    height: 100%;

    display: grid;
    grid-template-areas:
        "icon name"
        "description description";
    grid-template-columns: minmax(48px, 1fr) minmax(0, 1fr);
    grid-template-rows: auto 1fr;
    gap: 18px 24px;
    justify-items: end;
    align-items: start;

    box-sizing: border-box;
    padding: 30px;

    text-align: end;
}

.cell img {
    grid-area: icon;

    position: absolute;
    left: 0;
    top: 0;
}

.cell .name {
    grid-area: name;

    font-weight: 700;
    font-size: 24px;
    color: rgba(255, 255, 255, 0.9);

    overflow-wrap: anywhere;
}

.cell .description {
    grid-area: description;

    display: flex;
    flex-direction: column;
    gap: 8px;
    line-height: 1.35;

    font-weight: 400;
    font-size: 24px;
    color: rgba(255, 255, 255, 0.7);
}

.heading {
    grid-area: header;

    width: 750px;
    height: 120px;

    font-weight: 700;
    font-size: 40px;
    color: rgba(255, 255, 255, 0.9);

    display: flex;
    justify-content: center;
    align-items: center;
}

.brands { grid-area: brands; }

.search { grid-area: search; }

.review { grid-area: review; }

.escort { grid-area: escort; }

.carHighAngleView {
    position: absolute;

    width: 578px;
    height: 385px;
}

.carHighAngleView:nth-child(1) {
    left: 922px;
    top: 415px;
    rotate: 180deg;
}

.carHighAngleView:nth-child(2) {
    left: 0;
    top: 316px;
}

@media (max-width: 1000px) {
    .sector3 {
        height: auto;
        grid-template-areas:
            "header header"
            "brands search"
            "review escort";
        grid-template-columns: repeat(2, minmax(0, 1fr));
        grid-template-rows: 120px repeat(2, minmax(230px, auto));
        grid-gap: 30px;
        padding: 40px 24px;
        box-sizing: border-box;
    }

    .heading { width: 100%; }
    .cell .name, .cell .description { font-size: 20px; }
    .cell .name { text-wrap: wrap; }
    .carHighAngleView { opacity: .65; }
}

@media (max-width: 700px) {
    .sector3 {
        height: auto;
        grid-template-areas:
            "header"
            "brands"
            "review"
            "search"
            "escort";
        grid-template-columns: minmax(0, 1fr);
        grid-template-rows: 100px repeat(4, minmax(206px, auto));
        gap: 20px;
        padding: 40px 16px;
        box-sizing: border-box;
    }

    .heading { width: 100%; height: 100px; font-size: 28px; }

    .cell:not(.heading) {
        min-height: 190px;
    }

    .cell {
        padding: 24px;
        grid-template-columns: 64px minmax(0, 1fr);
        grid-template-rows: auto 1fr;
        gap: 18px;
        justify-items: start;
        text-align: start;
    }

    .cell img { position: static; width: 38px; height: 38px; }
    .cell .name { font-size: 20px; text-wrap: wrap; }
    .cell .description {
        font-size: 16px;
        line-height: 1.45;
        gap: 6px;
        color: var(--color-secondary-90);
    }

    .carHighAngleView {
        display: block;
        width: 220px;
        height: auto;
        opacity: .2;
        pointer-events: none;
    }

    .carHighAngleView:nth-child(1) {
        top: 360px;
        right: -90px;
        left: auto;
    }

    .carHighAngleView:nth-child(2) {
        top: 740px;
        left: -100px;
    }
}
</style>
