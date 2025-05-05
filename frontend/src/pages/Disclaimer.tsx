import { Col, Row, Card, Container, Button } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';

import { useCookies } from 'react-cookie';

export const Disclaimer = () => {

    const [cookies, setCookie] = useCookies(['userStarted']);

    const startQuestionnaire = () => {
        setCookie('userStarted', false, { path: '/' });
        navigate('/form');
    };


    const navigate = useNavigate();
  return (
    <>
    <Container className="p-0 m-0"> {/* Removed margin, border, and padding */}
                <h1 style={{ fontSize: '5rem', fontWeight: 'bold' }}>
                    Despre Aplicație
                </h1>
                <p style={{ fontStyle: 'italic' }}>
                    Și limitările acesteia.
                </p>
                <Row className="mb-5 mt-5 justify-content-start">
                    <Col md={6} className="d-flex justify-content-center">
                        <Card className="text-center">
                            <Card.Body>
                                <Card.Title style={{ fontSize: '2.5rem', fontWeight: 'bold' }}>Răspunsul nu este un diagnostic</Card.Title>
                                <Card.Text>
                                    Aplicația nu suplinează un specialist, ci este un simplu instrument pentru vă ajuta să înțelegeți starea dumneavoastră actuală, oferind o sugestie la final în vederea ușurării procesului de contactare a unui specialist.
                                </Card.Text>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
                <Row className="mb-5 justify-content-end">
                    <Col md={6} className="d-flex justify-content-center">
                        <Card className="text-center">
                            <Card.Body>
                                <Card.Title style={{ fontSize: '2.5rem', fontWeight: 'bold' }}>Explicabilitate</Card.Title>
                                <Card.Text>
                                    Aplicația utilizează un model AI ce furnizează răspunsuri pe baza unor formulare de specialitate. Deciziile pe care le ia acesta, sunt create prin relații probabiliste.
                                </Card.Text>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
                <Row className="mb-5 justify-content-center">
                    <Col md={6} className="d-flex justify-content-center">
                        <Card className="text-center">
                            <Card.Body>
                                <Card.Title style={{ fontSize: '2.5rem', fontWeight: 'bold' }}>Confidențialitate</Card.Title>
                                <Card.Text>
                                    Răspunsurile dumneavoastră <strong>sunt</strong> anonime, iar datele dumneavoastră nu vor fi folosite pentru alte scopuri decât cele legate de funcționarea aplicației.
                                </Card.Text>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
                <Button variant="dark" className="mt-4" onClick={() => startQuestionnaire()}>
                    Începe chestionarul.
                </Button>
    </Container>
    </>
  )
}

