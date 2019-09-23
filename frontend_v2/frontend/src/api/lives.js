export default function (cli) {
    return {
      list (page) {
        let offset = page * 20;
        return cli.get(`lives/?limit=${20}&offset=${offset}`)
      },
    }
  }