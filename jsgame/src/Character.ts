import { Canvas } from "../lib/Canvas";
import { Keyboard } from "../lib/Keyboard";
import { Ground } from "./Ground";

class Character {
    x: number
    y: number
    yVelocity: number
    width: number
    height: number
    speed: number
    color: string
    isGrounded: boolean

    constructor(
        x: number,
        y: number,
        width: number,
        height: number,
        speed: number,
        color: string
    ) {
        this.x = x;
        this.y = y;
        this.yVelocity = 0;
        this.width = width;
        this.height = height;
        this.speed = speed;
        this.color = color;
        this.isGrounded = false;
    }
    render(canvas: Canvas) {
        canvas.fillRectangle(this.x, this.y, this.width, this.height, this.color);
    }
    move(keyboard: Keyboard) {
        if (keyboard.keys('d'))
            this.x += this.speed;
        if (keyboard.keys('a'))
            this.x -= this.speed;

        if (this.isGrounded == true) 
            if (keyboard.keys(' '))
                this.yVelocity = 20;
    }   
    gravity(ground: Ground) {
        if (this.y > (ground.y + ground.height / 2) + this.height/2) {
            this.yVelocity -= 1; this.isGrounded = false
        } else {
            this.isGrounded = true; this.yVelocity = 0
        }
    }
    
    update() {
        this.y += this.yVelocity
    }
}

export { Character }