export const DEBUG = true;

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
