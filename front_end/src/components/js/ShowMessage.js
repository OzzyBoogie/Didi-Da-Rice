import {ElMessage} from "element-plus";

export  function showMessage(str, type) {
    ElMessage({
        message: str,
        type: type,
    })
}