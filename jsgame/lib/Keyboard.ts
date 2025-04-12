class Keyboard {
    private _keys: { [key: string]: boolean } = {};
  
    public keys(...keys: string[]): boolean {
      return keys.every((key) => this._keys[key]);
    }
    initialize() {
      document.addEventListener("keydown", (event) => {
        this._keys[event.key] = true;
      });
      document.addEventListener("keyup", (event) => {
        this._keys[event.key] = false;
      });
    }
  }
  
  export { Keyboard };
  