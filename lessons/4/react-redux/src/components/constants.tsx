function constructorConstantStore(uniqueName: string) {
  // TODO generator(uuid) - unique
  return {
    load: `load_${uniqueName}`,
    success: `success_${uniqueName}`,
    fail: `fail_${uniqueName}`,
    error: `error_${uniqueName}`,
    reset: `reset_${uniqueName}`,
    default: `default_${uniqueName}`,
  };
}

export const DEBUG = true;

// todo
// export const loadTodoList = "loadTodoList";
// export const successTodoList = "successTodoList";
// export const failTodoList = "failTodoList";
// export const errorTodoList = "errorTodoList";
// export const resetTodoList = "resetTodoList";

export const todoList = constructorConstantStore("todoList");
export const todoDetail = constructorConstantStore("todoDetail");
