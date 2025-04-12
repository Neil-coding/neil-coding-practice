import { Canvas } from "../lib/Canvas";

class Ground {
    constructor(
        public x: number,
        public y: number,
        public width: number,
        public height: number,
        public color: string
    ) { }
    render(canvas: Canvas) {
        canvas.fillRectangle(this.x, this.y, this.width, this.height, this.color);
    }
}

export { Ground }