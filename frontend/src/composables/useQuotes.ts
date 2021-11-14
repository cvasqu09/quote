import useMakeRequest from "./useMakeRequest";
import { ref } from "vue";
import { HTTPMethod } from "../utils/http";

export enum QuoteType {
  ALL = "all",
  TOP = "top",
}

export default () => {
  const { makeRequest, loading } = useMakeRequest();

  const getQuotes = async (type?: QuoteType) => {
    let url = "quote";
    if (type) {
      url += `?type=${type}`;
    }
    try {
      return await makeRequest(url, HTTPMethod.GET);
    } catch (e) {
      return [];
    }
  };

  return { getQuotes, loading };
};
