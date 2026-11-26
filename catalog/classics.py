from dataclasses import dataclass


@dataclass(frozen=True)
class ClassicBook:
    slug: str
    title: str
    author: str
    genre: str
    language: str
    description: str
    extract: str

    @property
    def coverPath(self):
        return f"catalog/covers/{self.slug}.jpg"


CLASSICS = (
    ClassicBook(
        "don-quijote-de-la-mancha", "Don Quijote de la Mancha", "Miguel de Cervantes",
        "Caballerías", "Español",
        "Un hidalgo manchego decide convertirse en caballero andante y sale al camino con Sancho Panza. "
        "Sus aventuras ponen frente a frente lo que imaginan los libros de caballerías y lo que encuentran al viajar.",
        "En un lugar de la Mancha, de cuyo nombre no quiero acordarme…",
    ),
    ClassicBook(
        "alicia-en-el-pais-de-las-maravillas", "Alicia en el país de las maravillas", "Lewis Carroll",
        "Fantasía", "Inglés",
        "Alicia sigue a un conejo blanco y cae en un mundo en el que el tamaño, el tiempo y las reglas cambian a cada paso.",
        "Alice was beginning to get very tired of sitting by her sister on the bank…",
    ),
    ClassicBook(
        "el-retrato-de-dorian-gray", "El retrato de Dorian Gray", "Oscar Wilde",
        "Novela gótica", "Inglés",
        "Dorian desea conservar su juventud. A medida que cambia su vida, el retrato que guarda en casa empieza a cambiar por él.",
        "The studio was filled with the rich odour of roses…",
    ),
    ClassicBook(
        "orgullo-y-prejuicio", "Orgullo y prejuicio", "Jane Austen",
        "Novela de costumbres", "Inglés",
        "Elizabeth Bennet y el señor Darcy revisan sus primeras impresiones en una sociedad donde el dinero y el matrimonio pesan.",
        "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.",
    ),
    ClassicBook(
        "frankenstein", "Frankenstein", "Mary Shelley",
        "Ciencia ficción", "Inglés",
        "Victor Frankenstein le da vida a una criatura y la abandona. El relato sigue las consecuencias de esa decisión.",
        "You will rejoice to hear that no disaster has accompanied the commencement of an enterprise…",
    ),
)
