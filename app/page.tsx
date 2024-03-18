'use client'
import React, { useEffect, useState } from "react"

export default function Home() {

  const [response, setResponse] = useState()

  async function hello() {
    const hello:any = await fetch(`/api/consultproduct`, {
      method: "GET",
      cache: "no-store",
      headers: {
        "content_type": "application/json",
      }
    })
      .then(response =>
          response.json()
      ).catch(err => console.error(err))

      setResponse(hello.message)
  }

  useEffect(() => {
    hello()
  }, [])

  return (
    <>
      <p>{response}</p>
    </>
  )
}
