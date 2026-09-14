<script setup lang="ts">

import { ref } from "vue";

import BlockGlass from "../components/BlockGlass.vue";

import { storeToRefs } from "pinia";
import BlockGlassButton from "../components/BlockGlassButton.vue";
import LoadingAnimation from "../components/LoadingAnimation.vue";
import TelegramIcon from "../assets/telegram.svg";
import VkIcon from "../assets/vk.svg";
import PhoneIcon from "../assets/phone.svg";
import { useStore } from "../stores/Store.ts";

const store = useStore()
const { car, carLoading } = storeToRefs(store)

const socials = [
    { name: 'Telegram', href: 'https://t.me/omegaautogroup?direct', icon: TelegramIcon },
    { name: 'ВКонтакте', href: 'https://vk.me/omegaautogroup', icon: VkIcon }
]

const phones = ['+7 (932) 301-89-98', "+7 (922) 700-90-90"]

const currentImageIndex = ref(0)

const goToSocial = (url: string) => { window.open(url, '_blank') }
const getPhoneHref = (phone: string) => `tel:${ phone.replace(/[^\d+]/g, '') }`
const callPhone = (phone: string) => { window.location.href = getPhoneHref(phone) }
const numberFormatted = (n: number) => new Intl.NumberFormat("ru-RU").format(Number(n))
const showPreviousImage = () => {
    const imageCount = car.value?.images?.length ?? 0
    if (!imageCount) return
    currentImageIndex.value = ( currentImageIndex.value - 1 + imageCount ) % imageCount
}
const showNextImage = () => {
    const imageCount = car.value?.images?.length ?? 0
    if (!imageCount) return
    currentImageIndex.value = ( currentImageIndex.value + 1 ) % imageCount
}
</script>

<template>
    <LoadingAnimation v-if="carLoading || !car"/>

    <template v-else>
        <div class="carPage">
            <div class="card">
                <div class="image-frame" style="grid-area: image">
                    <img :src="car?.images?.at(currentImageIndex)?.image" alt="Car Image" class="background"/>
                    <img :src="car?.images?.at(currentImageIndex)?.image" alt="Car Image" class="foreground"/>

                    <block-glass-button class="gallery-arrow gallery-arrow-left" type="button"
                                        aria-label="Предыдущее изображение" @click="showPreviousImage">
                        &#10094;
                    </block-glass-button>

                    <block-glass-button class="gallery-arrow gallery-arrow-right" type="button"
                                        aria-label="Следующее изображение" @click="showNextImage">
                        &#10095;
                    </block-glass-button>
                </div>

                <block-glass class="info" style="grid-area: info">
                    <text class="name" style="grid-area: name"><b>{{ car?.brand + ' ' + car?.model }}</b></text>

                    <text class="year" style="grid-area: year">
                        <span><b>Год</b></span>
                        <span>{{ car?.year }}</span>
                    </text>

                    <text class="mileage" style="grid-area: mileage">
                        <span><b>Пробег</b></span>
                        <span>{{ numberFormatted(car?.mileage || 0) }} км</span>
                    </text>

                    <text class="power" style="grid-area: power">
                        <span><b>Мощность</b></span>
                        <span>{{ car?.power }} л.с.</span>
                    </text>

                    <text class="displacement" style="grid-area: displacement">
                        <span><b>Объем</b></span>
                        <span>{{ car?.displacement }} л</span>
                    </text>

                    <text class="gear" style="grid-area: gear">
                        <span><b>Коробка</b></span>
                        <span>{{ car?.gear }}</span>
                    </text>

                    <text class="color" style="grid-area: color">
                        <span><b>Цвет</b></span>
                        <span>{{ car?.color }}</span>
                    </text>

                    <text class="fuel" style="grid-area: fuel">
                        <span><b>Топливо</b></span>
                        <span>{{ car?.fuel }}</span>
                    </text>

                    <text class="price" style="grid-area: price">
                        <span><b>{{ numberFormatted(car?.price || 0) }} ¥</b></span>
                    </text>
                </block-glass>

                <div class="gallery" style="grid-area: gallery">
                    <div class="image-frame" v-for="(image, index) in car?.images" :key="image.index"
                         :style="`filter: brightness(${index===currentImageIndex ? '1' : '0.7'})`">
                        <img :src="image.image" alt="Car Image" @click="currentImageIndex = index"/>
                    </div>
                </div>

                <block-glass class="links" style="grid-area: links">
                    <text>
                        <span><b>Понравился автомобиль?</b></span>
                        <span>Обратитесь к нам по одному из способов, указанных ниже</span>
                    </text>

                    <div class="buttons" style="grid-area: buttons">
                        <button v-for="social in socials" :key="social.name" type="button"
                                @click="goToSocial(social.href)">
                            <img :src="social.icon" :alt="social.name"/>
                            <span>{{ social.name }}</span>
                        </button>

                        <button v-for="phone in phones" :key="phone" type="button" @click="callPhone(phone)">
                            <img :src="PhoneIcon" alt="Phone"/>
                            <span>{{ phone }}</span>
                        </button>
                    </div>
                </block-glass>
            </div>
        </div>
    </template>
</template>

<style scoped>
.carPage {
    position: relative;

    display: flex;
    flex-direction: column;

    box-sizing: border-box;
    padding: 120px 0;
    gap: 100px;
}

.card {
    width: 100%;

    display: grid;
    grid-template-areas:
        "image info"
        "gallery links";
    grid-template-columns: 900px minmax(0, 1fr);
    grid-template-rows: 600px auto;
    grid-column-gap: 50px;
    grid-row-gap: 25px;
}

.image-frame {
    position: relative;

    width: 900px;
    height: 600px;

    box-sizing: border-box;
    border-radius: 30px;

    overflow: hidden;
}

.image-frame img {
    width: 100%;
    height: 100%;

    object-fit: contain;
}

.image-frame .background {
    position: absolute;
    inset: 0;

    width: 100%;
    height: 100%;

    object-fit: cover;
    filter: blur(30px) brightness(0.7);
    transform: scale(1.1);
    z-index: 0;
    pointer-events: none;
}

.image-frame .foreground {
    position: relative;
    z-index: 1;
    display: block;
}

.gallery-arrow {
    position: absolute;
    top: 50%;
    z-index: 2;

    display: flex;
    align-items: center;
    justify-content: center;

    width: 56px;
    height: 56px;
    aspect-ratio: 1;
    border-radius: 50% !important;

    color: rgba(255, 255, 255, 0.9);
    font-size: 32px;
    line-height: 1;
    cursor: pointer;

    transform: translateY(-50%);

    user-select: none;
}

.gallery-arrow-left {
    left: 24px;
}

.gallery-arrow-right {
    right: 24px;
}

.info {
    width: 100%;
    height: 100%;

    display: grid;
    grid-template-areas:
        "name name"
        "year mileage"
        "power displacement"
        "gear color"
        "fuel ."
        "price price";
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(6, 1fr);

    padding: 30px 50px;
    box-sizing: border-box;
}

.info text {
    display: flex;
    flex-direction: column;
}

.info text {
    font-size: 24px;
    font-weight: 300;
    color: rgba(255, 255, 255, 0.7);
}

.info text b {
    font-weight: 700;
}

.info .name, .info .price {
    color: rgba(255, 255, 255, 0.9);
    font-size: 48px;
}

.gallery {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    align-self: start;

    width: 900px;
    height: fit-content;
    gap: 10px;

    border-radius: 30px;

    overflow: hidden;
}

.gallery .image-frame {
    width: 172px;
    height: 115px;
    overflow: hidden;
    border-radius: 0;

    box-sizing: border-box;
}

.gallery .image-frame img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.links {
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: start;

    height: fit-content;

    gap: 40px;

    box-sizing: border-box;
    padding: 30px 30px;

    font-size: 15px;
    font-weight: 300;
    color: rgba(255, 255, 255, 0.7);

    b {
        font-size: 24px;
        font-weight: 700;
        color: rgba(255, 255, 255, 0.9);
    }
}

.links > text {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.links .buttons {
    display: grid;
    grid-template-columns: 2fr 3fr;
    grid-template-rows: repeat(2, 1fr);
    grid-gap: 10px;
    grid-auto-flow: column;

    width: 100%;
}

.links button {
    all: unset;

    position: relative;
    display: flex;
    align-items: center;

    box-sizing: border-box;
    padding: 0 35px;

    font-size: 16px;
    font-weight: 400;
    line-height: 1.25;

    width: 100%;
    cursor: pointer;

    img {
        position: absolute;
        height: 15px;

        left: 0;
        top: 50%;

        transform: translateY(-50%);
    }

    span {
        display: block;
        will-change: transform, color;
        transition: transform 0.3s ease-out, color 0.3s ease-out;
    }
}

.links button:hover span {
    color: rgba(255, 255, 255, 0.9);
    transform: translateY(-10%);
}

@media (max-width: 1180px) {
    .carPage {
        padding: 120px 24px;
    }

    .card {
        grid-template-areas:
            "image"
            "info"
            "gallery"
            "links";
        grid-template-columns: minmax(0, 1fr);
        grid-template-rows: auto;
        gap: 24px;
    }

    .image-frame {
        width: 100%;
        height: auto;
        aspect-ratio: 3 / 2;
    }

    .info { min-height: 480px; }

    .gallery {
        display: grid;
        grid-template-columns: repeat(5, minmax(0, 1fr));
        width: 100%;
    }

    .gallery .image-frame {
        width: 100%;
        height: auto;
        aspect-ratio: 3 / 2;
    }

    .links { width: 100%; }
}

@media (max-width: 700px) {
    .carPage {
        max-height: none;
        padding: 100px 16px 100px;
    }

    .card { gap: 16px; }

    .gallery { grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px; }

    .gallery-arrow {
        width: 44px;
        height: 44px;
        font-size: 24px;
    }

    .gallery-arrow-left { left: 12px; }

    .gallery-arrow-right { right: 12px; }

    .info {
        min-height: 430px;
        padding: 20px;
    }

    .info text {
        min-width: 0;
        overflow-wrap: anywhere;
        font-size: clamp(15px, 4vw, 18px);
        color: var(--color-secondary-90);
    }

    .info .name,
    .info .price { font-size: clamp(25px, 8vw, 34px); }

    .links {
        gap: 24px;
        padding: 24px 20px;
        color: var(--color-secondary-90);
    }

    .links .buttons {
        grid-template-columns: 1fr 1fr;
        grid-template-rows: repeat(2, minmax(44px, auto));
        grid-auto-flow: row;
    }

    .links button {
        min-height: 44px;
        font-size: 14px;
    }
}

@media (max-width: 480px) {
    .links .buttons {
        grid-template-columns: minmax(0, 1fr);
        grid-template-rows: repeat(4, 44px);
    }
}
</style>
