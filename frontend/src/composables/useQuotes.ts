import useMakeRequest from "./useMakeRequest";
import { ref } from "vue";
import { HTTPMethod } from "../utils/http";

export enum QuoteType {
  ALL = "all",
  TOP = "top",
}

export default () => {
  const { makeRequest, loading } = useMakeRequest();

  const getQuotes = async (type: QuoteType, searchText?: string) => {
    let url = "quote/?";
    url += `type=${type}`;

    if (searchText) {
      url += `&search=${searchText}`;
    }

    try {
      console.log("calling");
      return await makeRequest(url, HTTPMethod.GET);
    } catch (e) {
      console.log("error");
      return [];
    }
  };

  return { getQuotes, loading };
};
