'use client'
import React, { useEffect, useState } from "react"

export default function Home() {

  const [response, setResponse] = useState()
  const [data, setData] = useState([])

  async function hello() {
    const hello:any = await fetch(`/api/consultproduct`, {
      method: "GET",
      cache: "no-store",
      headers: {
        "content_type": "application/json",
        "Keep-Alive": 'timeout=5, max=1000'
      }
    })
      .then(response =>
          response.json()
      ).catch(err => console.error(err))

      setResponse(hello.message)
      setData(hello.data)
  }

  useEffect(() => {
    hello()
  }, [])

  return (
    <>
      <p>{response}</p>
      <ul>
        {data.map((element:any) => (
          <li>{element.marca}</li>
        ))}
      </ul>
    </>
  )
}
