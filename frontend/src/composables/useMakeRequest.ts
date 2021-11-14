import { ref } from "vue";
import http, { HTTPMethod } from "../utils/http";

export default () => {
  const loading = ref(false);

  const makeRequest = async (url: string, method: HTTPMethod, data = null) => {
    loading.value = true;
    const response = await http({
      method,
      url,
      data: data ? data : undefined,
    });
    loading.value = false;
    return response;
  };

  return {
    loading,
    makeRequest,
  };
};
