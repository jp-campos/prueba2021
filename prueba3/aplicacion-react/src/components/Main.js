
import { Field, Form, Formik } from "formik";
import React, { useState } from 'react';

const ENDPOINT = 'http://127.0.0.1:8000/'
function Main(){

    const[payloadRes, setPayloadRes] = useState('')
    const[submitRes, setSubmitRes] = useState('')

    async function handleEnviar(values){
        
        let rGet = await fetch(ENDPOINT + 'createPayload')
        
        let rGetText = await rGet.text()
        
        setPayloadRes(rGetText)
       
        let payloadId = rGet.payloadId
        
        let bodyPost = {'payloadId':''+payloadId, 'nombre':values.nombre,'apellido':values.apellido }

        let rPost = await fetch(ENDPOINT + 'submit',{method:'POST',body:JSON.stringify(bodyPost), headers: {'Content-Type': 'application/json'}})
        let rPostText = await rPost.text()
        setSubmitRes(rPostText)

        
    }

    return(
    <section className="card-container">
        
        <article className="card">
            <h3 className="titulo-card">Inserte sus datos por favor</h3>
            <hr></hr>
            <Formik
                initialValues={{ palabra: "" }}
                onSubmit={(values, { resetForm }) => {
                  handleEnviar(values, resetForm);
                }}
              >
                <Form>
                  <div className="form">
                    <h5 className="nombre-campo">Nombre</h5>
                    <Field
                      className="input"
                      autoComplete="off"
                      name="nombre"
                      type="text"
                    ></Field>
                    <h5 className="nombre-campo">Apellido</h5>
                    <Field
                      className="input"
                      autoComplete="off"
                      name="apellido"
                      type="text"
                    ></Field>
                    <div className="boton-wrap">
                        <button  type="submit">Enviar </button>
                    </div>
                   
                  </div>
                </Form>
              </Formik>

        </article>

        <article className="card right-card">
           { payloadRes?  <h4 className="nombre-campo">Primer Response</h4>: ''}
            <code className="response">{payloadRes}</code>
            {payloadRes?  <hr/>: ''}
            { submitRes?  <h4 className="nombre-campo">Segundo Response</h4>: ''}
            <code className="response">{submitRes}</code>
        </article>
    </section>
    )

}


export default Main