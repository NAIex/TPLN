import { Col, Row, Container, Button, Card } from 'react-bootstrap'
import { useNavigate } from 'react-router-dom'

export const LandingPage = () => {

    const navigate = useNavigate()

  return (
    <>
    <Container className="p-0 m-0"> {/* Removed margin, border, and padding */}
                <h1 style={{ fontSize: '5rem', fontWeight: 'bold' }}>
                    MediQA 
                </h1>
                <p style={{ fontStyle: 'italic' }}>
                    Discover Your Path to Wellness
                </p>
                <Row className="mb-5 mt-5 justify-content-start">
                    <Col md={6} className="d-flex justify-content-center">
                        <Card className="text-center">
                            <Card.Body>
                                <Card.Title style={{ fontSize: '2.5rem', fontWeight: 'bold' }}>Step 1</Card.Title>
                                <Card.Text>
                                    Begin your journey by understanding the importance of mental health. This step emphasizes the need for self-awareness and recognizing the signs of stress and anxiety. By taking the time to reflect on your feelings, you can set the foundation for a healthier mindset.
                                </Card.Text>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
                <Row className="mb-5 justify-content-end">
                    <Col md={6} className="d-flex justify-content-center">
                        <Card className="text-center">
                            <Card.Body>
                                <Card.Title style={{ fontSize: '2.5rem', fontWeight: 'bold' }}>Step 2</Card.Title>
                                <Card.Text>
                                    In this step, we focus on physical wellness. Engaging in regular exercise and maintaining a balanced diet are crucial for overall health. This step encourages you to explore different activities that you enjoy, making fitness a fun part of your daily routine.
                                </Card.Text>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
                <Row className="mb-5 justify-content-center">
                    <Col md={6} className="d-flex justify-content-center">
                        <Card className="text-center">
                            <Card.Body>
                                <Card.Title style={{ fontSize: '2.5rem', fontWeight: 'bold' }}>Step 3</Card.Title>
                                <Card.Text>
                                    The final step is about building a supportive community. Surrounding yourself with positive influences and seeking help when needed can significantly impact your wellness journey. This step encourages you to connect with others and share your experiences.
                                </Card.Text>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
                <Button variant="dark" className="mt-4" onClick={() => navigate('/disclaimer')}>
                    Despre Chestionar.
                </Button>
                
    </Container>
    </>
  )
}
