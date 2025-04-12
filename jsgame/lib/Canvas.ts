class Canvas {
    width: number;
    height: number;
    protected ctx: CanvasRenderingContext2D;
  
    constructor() {
      var canvas = document.querySelector("canvas") as HTMLCanvasElement;
      this.width = canvas.width = window.innerWidth;
      this.height = canvas.height = window.innerHeight;
      this.ctx = canvas.getContext("2d") as CanvasRenderingContext2D;
      this.setup();
    }
    centerOrigin() {
      this.ctx.translate(this.width / 2, this.height / 2);
    }
    flipYAxis() {
      this.ctx.scale(1, -1);
    }
    setup() {
      this.centerOrigin();
      this.flipYAxis();
    }
    erase() {
      this.ctx.clearRect(
        0 - this.width / 2,
        0 - this.height / 2,
        this.width * 2,
        this.height * 2
      );
    }
    fillRectangle(
      x: number,
      y: number,
      width: number,
      height: number,
      color: string
    ) {
      this.ctx.fillStyle = color;
      this.ctx.fillRect(x - width / 2, y - height / 2, width, height);
    }
    strokeRectangle(
      x: number,
      y: number,
      width: number,
      height: number,
      color: string
    ) {
      this.ctx.strokeStyle = color;
      this.ctx.strokeRect(x - width / 2, y - height / 2, width, height);
    }
    fillCircle(x: number, y: number, radius: number, color: string) {
      this.ctx.fillStyle = color;
      this.ctx.beginPath();
      this.ctx.arc(x, y, radius, 0, Math.PI * 2, false);
      this.ctx.fill();
      this.ctx.closePath();
    }
    strokeCircle(x: number, y: number, radius: number, color: string) {
      this.ctx.strokeStyle = color;
      this.ctx.beginPath();
      this.ctx.arc(x, y, radius, 0, Math.PI * 2, false);
      this.ctx.stroke();
      this.ctx.closePath();
    }
    line(
      x1: number,
      y1: number,
      x2: number,
      y2: number,
      color: string,
      thickness: number,
      dash: number[] = []
    ) {
      this.ctx.strokeStyle = color;
      this.ctx.lineWidth = thickness;
      this.ctx.beginPath();
      this.ctx.setLineDash(dash);
      this.ctx.moveTo(x1, y1);
      this.ctx.lineTo(x2, y2);
      this.ctx.stroke();
      this.ctx.closePath();
    }
    drawXAxis(interval = 30, notchSize = 10, color = "black") {
      this.line(-this.width / 2, 0, this.width / 2, 0, color, 1);
      for (var i = -this.width / 2; i < this.width / 2; i += interval) {
        this.line(i, -notchSize / 2, i, notchSize / 2, color, 1);
      }
    }
    drawYAxis(interval = 30, notchSize = 10, color = "black") {
      this.line(0, -this.height / 2, 0, this.height / 2, color, 1);
      for (var i = -this.height / 2; i < this.height / 2; i += interval) {
        this.line(-notchSize / 2, i, notchSize / 2, i, color, 1);
      }
    }
    drawAxes(interval = 30, notchSize = 10, color = "black") {
      this.drawXAxis(interval, notchSize, color);
      this.drawYAxis(interval, notchSize, color);
    }
  }
  
  export { Canvas }