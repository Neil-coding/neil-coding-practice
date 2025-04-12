class Mouse {
    leftClick: boolean;
    rightClick: boolean;
  
    constructor() {
      this.leftClick = false;
      this.rightClick = false;
    }
    initialize() {
      document.addEventListener("mousedown", (event) => {
        if (event.button === 0) {
          this.leftClick = true;
        } else if (event.button === 2) {
          this.rightClick = true;
        }
      });
      document.addEventListener("mouseup", (event) => {
        if (event.button === 0) {
          this.leftClick = false;
        } else if (event.button === 2) {
          this.rightClick = false;
        }
      });
    }
  }
  export { Mouse };
  