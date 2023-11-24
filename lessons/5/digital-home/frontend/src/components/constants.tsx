export const DEBUG = true; // if host is 127.0.0.1:3000

function constructorConstant(name: string) {
  return {
    load: `load_${name}`,
    success: `success_${name}`,
    fail: `fail_${name}`,
    error: `error_${name}`,
    reset: `reset_${name}`,
  };
}

export const messageList = constructorConstant("messageList");
// export const messageDetail = constructorConstant("messageDetail");
export const nowMessageList = constructorConstant("nowMessageList");
export const constantUserRegister = constructorConstant("constantUserRegister");
