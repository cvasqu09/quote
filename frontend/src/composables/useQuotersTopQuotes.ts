import { HTTPMethod } from "@/utils/http";
import useMakeRequest from "@/composables/useMakeRequest";
import { ref } from "vue";

export default () => {
  const { makeRequest, loading: quotersTopQuotesLoading } = useMakeRequest();

  const quotersTopQuotes = ref([]);
  const getQuotersTopQuotes = async (quoterId: string) => {
    const url = `quoter/${quoterId}/quotes`;

    try {
      console.log("quoters top quotes");
      const response = await makeRequest(url, HTTPMethod.GET);
      quotersTopQuotes.value = response.data;
    } catch (e) {
      quotersTopQuotes.value = [];
    }
  };

  return { getQuotersTopQuotes, quotersTopQuotes, quotersTopQuotesLoading };
};
