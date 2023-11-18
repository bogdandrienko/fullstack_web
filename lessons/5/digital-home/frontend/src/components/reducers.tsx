export function constructorReducer({ load, success, fail, error, reset }: any) {
  return function (state = {}, action: { type: string; payload: any }) {
    switch (action.type) {
      case load:
        return { load: true };
      case success:
        return { load: false, data: action.payload };
      case fail:
        return { load: false, fail: action.payload };
      case error:
        return { load: false, error: action.payload };
      case reset:
        return { load: true };
      default:
        return state;
    }
  };
}
