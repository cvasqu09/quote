import useMakeRequest from "./useMakeRequest";
import { HTTPMethod } from "../utils/http";

export enum QuoterType {
  TOP = "top",
}

export default () => {
  const { makeRequest, loading: quotersLoading } = useMakeRequest();

  const getQuoters = async (type: QuoterType) => {
    let url = "quoter/?";
    url += `type=${type}`;

    try {
      console.log("making request");
      return await makeRequest(url, HTTPMethod.GET);
    } catch (e) {
      return [];
    }
  };

  return { getQuoters, quotersLoading };
};
